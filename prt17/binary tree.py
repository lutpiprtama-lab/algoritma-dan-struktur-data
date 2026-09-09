class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


# Membuat node
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")
I = Node("I")
J = Node("J")

# Membentuk tree
A.add_child(B)
A.add_child(C)

B.add_child(D)
B.add_child(E)

C.add_child(F)

E.add_child(G)
E.add_child(H)

G.add_child(I)
G.add_child(J)

# Parent dictionary
parent = {
    "B": "A",
    "C": "A",
    "D": "B",
    "E": "B",
    "F": "C",
    "G": "E",
    "H": "E",
    "I": "G",
    "J": "G"
}


# ==========================
# ROOT
# ==========================
print("ROOT :", A.data)

# ==========================
# NODE
# ==========================
print("\nNODE :")
for n in ["A","B","C","D","E","F","G","H","I","J"]:
    print(n, end=" ")

# ==========================
# PARENT
# ==========================
print("\n\nPARENT :")
for child, par in parent.items():
    print(f"Parent({child}) = {par}")

# ==========================
# CHILD
# ==========================
print("\nCHILD :")
nodes = [A,B,C,D,E,F,G,H,I,J]

for node in nodes:
    if node.children:
        print(f"Child({node.data}) =",
              [c.data for c in node.children])

# ==========================
# LEAF
# ==========================
print("\nLEAF :")
for node in nodes:
    if len(node.children) == 0:
        print(node.data, end=" ")

# ==========================
# SIBLING
# ==========================
print("\n\nSIBLING :")
print("B dan C")
print("D dan E")
print("G dan H")
print("I dan J")

# ==========================
# DEGREE
# ==========================
print("\nDEGREE :")
for node in nodes:
    print(f"Degree({node.data}) = {len(node.children)}")

# ==========================
# DEPTH
# ==========================
depth = {
    "A":0,
    "B":1,
    "C":1,
    "D":2,
    "E":2,
    "F":2,
    "G":3,
    "H":3,
    "I":4,
    "J":4
}

print("\nDEPTH :")
for node, d in depth.items():
    print(f"Depth({node}) = {d}")

# ==========================
# ANCESTOR
# ==========================
print("\nANCESTOR J :")
print("A -> B -> E -> G")

# ==========================
# DESCENDANT
# ==========================
print("\nDESCENDANT B :")
print("D, E, G, H, I, J")

# ==========================
# PREDECESSOR
# ==========================
print("\nPREDECESSOR G :")
print("A -> B -> E")

# ==========================
# SUCCESSOR
# ==========================
print("\nSUCCESSOR E :")
print("G, H, I, J")

# ==========================
# SIZE
# ==========================
print("\nSIZE TREE :")
print("10 Node")

# ==========================
# HEIGHT
# ==========================
print("\nHEIGHT TREE :")
print("4")

# ==========================
# SUBTREE
# ==========================
print("\nSUBTREE E :")
print("""
      E
     / \\
    G   H
   / \\
  I   J
""")

# ==========================
# FOREST
# ==========================
print("\nFOREST :")
print("Jika node A dihapus maka terbentuk:")
print("Tree B dan Tree C")