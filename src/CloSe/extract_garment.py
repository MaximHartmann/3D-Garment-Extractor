import pickle
import torch
import trimesh
import numpy as np
import os

LABEL2CLASS = [
    'Hat', 'Body', 'Shirt', 'TShirt', 'Vest', 'Coat', 'Dress', 'Skirt', 
    'Pants', 'ShortPants', 'Shoes', 'Hoodies', 'Hair', 'Swimwear', 
    'Underwear', 'Scarf', 'Jumpsuits', 'Jacket'
]

npz_path = 'my_scan.npz'

pkl_path = 'out/demo_scan_out/outputs.pkl'
if not os.path.exists(pkl_path):
    print(f"Fehler: {pkl_path} nicht gefunden!")
    exit()

print(f"Öffne {pkl_path}...")
with open(pkl_path, 'rb') as f:
    data = pickle.load(f)
    
scan_data = np.load(npz_path)
original_faces = scan_data['faces']

points = torch.vstack(data['points']).numpy()
labels = torch.cat(data['labels']).numpy()

xyz = points[:, :3]
rgb = points[:, 3:6]

gefundene_labels = np.unique(labels)
print(f"Die KI hat folgende Segmente im Modell erkannt: {gefundene_labels}")

for lbl in gefundene_labels:
    lbl_idx = int(lbl)
    class_name = LABEL2CLASS[lbl_idx] if lbl_idx < len(LABEL2CLASS) else f"Unknown_{lbl_idx}"
        
    point_mask = (labels == lbl)
        
    faces_in_garment = point_mask[original_faces].sum(axis=1) >= 2
    extracted_faces = original_faces[faces_in_garment]
    
    if len(extracted_faces) == 0:
        continue
    
    mesh = trimesh.Trimesh(vertices=xyz, faces=extracted_faces, vertex_colors=rgb, process=False)
    
    mesh.remove_unreferenced_vertices()
    
    out_name = f'out/demo_scan_out/mesh_{class_name}.ply'
    mesh.export(out_name)
    
    print(f"3D-Mesh gespeichert: {out_name} ({len(mesh.vertices)} Punkte, {len(mesh.faces)} Flächen)")