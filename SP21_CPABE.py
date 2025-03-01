from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, GT, pair, hashPair
from charm.toolbox.secretutil import SecretUtil
from charm.toolbox.ABEnc import ABEnc, Input, Output
from charm.toolbox.symcrypto import SymmetricCryptoAbstraction
from charm.toolbox.policytree import PolicyParser
from Zeropoly import Zero_poly
from QueryDB import connect, UploadData, QueryData

# type annotations
pk_t = {'g_2': G1, 'h_i': G2, 'e_gg_alpha': GT}
mk_t = {'alpha': ZR, 'g': G1}
sk_t = {'dk': G1, 'B': str}
ct_t = {'C': GT, 'C1': G1, 'C2': G2, 'policy': str}

debug = False

class CPabe_SP21(ABEnc):

    def __init__(self, groupObj):
        ABEnc.__init__(self)
        global util, group
        util = SecretUtil(groupObj, verbose=False)
        group = groupObj

    @Output(pk_t, mk_t)
    def setup(self, uni_size):
        g, h, alpha = group.random(G1), group.random(G2), group.random(ZR)
        g.initPP()
        h.initPP()
        g_2 = g ** (alpha**2)
        e_gg_alpha = pair(g, h) ** alpha
        h_i = {}
        for j in range(uni_size + 1):
            h_i[j] = h ** (alpha ** j)
        pk = {'g_2': g_2, 'h_i': h_i, 'e_gg_alpha': e_gg_alpha}
        mk = {'alpha': alpha, 'g': g}
        return (pk, mk)

    @Input(pk_t, mk_t, [str], [str])
    @Output(sk_t)
    def keygen(self, pk, mk, B, U):
        S = list(set(U) - set(B))
        Zerop = 1
        for attrs in S:
            Zerop *= mk['alpha'] + group.hash(attrs, ZR)
        dk = mk['g'] ** (1 / Zerop)
        return {'dk': dk, 'B': B}

    @Input(pk_t, bytes, str, [str])
    @Output(dict)
    def encrypt(self, pk, M, P, U):
        M_GT = group.random(GT)
        # Symmetric encryption of the message
        sym_key = hashPair(M_GT)
        sym_crypto = SymmetricCryptoAbstraction(sym_key)
        ct_sym = sym_crypto.encrypt(M)
        
        # ABE encryption of the symmetric key
        a=[]; C2=1
        Com_set= list(set(U) - set(P))
        for attrs in Com_set:
            a.append(group.hash(attrs, ZR))

        (indices,coeff_mult)=Zero_poly(a,len(a)-1,[0],[1])
        Coeffs=list(reversed(coeff_mult))

        for i in range(len(indices)):
            C2*= (pk['h_i'][i+1] ** Coeffs[i])

        r = group.random(ZR)     
        C = M_GT * (pk['e_gg_alpha'] ** r)
        C1 = pk['g_2'] ** (-r)
        C2 = C2 ** r
        ct_abe = {'C': C, 'C1': C1, 'C2': C2, 'policy': P}

        return {'ct_sym': ct_sym, 'ct_abe': ct_abe}

    @Input(pk_t, sk_t, dict)
    @Output(bytes)
    def decrypt(self, pk, sk, ct):
        ct_sym = ct['ct_sym']
        ct_abe = ct['ct_abe']

        # ABE decryption to get the symmetric key
        A=list(set(sk['B'])-set(ct['policy']))
        a=[]; z=1
        for attrs in A:
            a.append(group.hash(attrs, ZR))
        (indices,coeff_mult)=Zero_poly(a,len(a)-1,[0],[1])
        Coeffs=list(reversed(coeff_mult))

        for i in range(len(indices)-1):
            z*= pk['h_i'][i] ** Coeffs[i+1]

        V=(pair(ct_abe['C1'],z) * pair(sk['dk'],ct_abe['C2']))
        M_GT = ct_abe['C'] * (V ** (-1 / Coeffs[0]))

        # Assuming the original sym_key
        sym_key = hashPair(M_GT)
        print("\n", hashPair(M_GT))
        # Symmetric decryption of the message
        sym_crypto = SymmetricCryptoAbstraction(sym_key)
        M = sym_crypto.decrypt(ct_sym)
        
        return M

# Example usage
groupObj = PairingGroup('SS512')
cpabe = CPabe_SP21(groupObj)

# Setup
uni_size = 10  # example universe size
(pk, mk) = cpabe.setup(uni_size)

# Key generation
attributes = ['ATTR1', 'ATTR2', 'ATTR3', 'ATTR4', 'ATTR5']
UserSet = ['ATTR1', 'ATTR2', 'ATTR3']
sk = cpabe.keygen(pk, mk, UserSet, attributes)

# Read file to bytes
f_path = 'files/note.txt'
extension = f_path.split('.')[-1]

with open(f_path, 'rb') as file:
    message = file.read()

# Encryption
policy = 'ATTR1 and ATTR2'
ct = cpabe.encrypt(pk, message, policy, attributes)\

# # Load ciphet text to mongoDB Atlas
# db = connect("Crypto")
# collection = db.EncodedData
# UploadData(groupObj, collection, ct, extension)
# ciphertext, extname = QueryData(groupObj, collection) # Query last data in database

# Decryption
decrypted_message = cpabe.decrypt(pk, sk, ct)
if (decrypted_message == message):
    print("\nMatch\n")
else:
    print("\nNot match\n")

# # Write bytes to file
# with open(f'check.{extname}', 'wb') as file:
#     file.write(decrypted_message)