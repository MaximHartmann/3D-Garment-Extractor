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

pkl_path = 'out/demo_scan_out/outputs.pkl'
if not os.path.exists(pkl_path):
    print(f"Fehler: {pkl_path} nicht gefunden!")
    exit()

print(f"Öffne {pkl_path}...")
with open(pkl_path, 'rb') as f:
    data = pickle.load(f)

points = torch.vstack(data['points']).numpy()
labels = torch.cat(data['labels']).numpy()

xyz = points[:, :3]
rgb = points[:, 3:6]

gefundene_labels = np.unique(labels)
print(f"Die KI hat folgende Segmente im Modell erkannt: {gefundene_labels}")

for lbl in gefundene_labels:
    lbl_idx = int(lbl)
    if lbl_idx < len(LABEL2CLASS):
        class_name = LABEL2CLASS[lbl_idx]
    else:
        class_name = f"Unknown_Label_{lbl_idx}"
        
    mask = (labels == lbl)
    extracted_xyz = xyz[mask]
    extracted_rgb = rgb[mask]
    
    print(f"-> Segment '{class_name}': {len(extracted_xyz)} Punkte.")
    
    if len(extracted_xyz) > 0:
        pc = trimesh.PointCloud(extracted_xyz, colors=extracted_rgb)
        out_name = f'out/demo_scan_out/extracted_{class_name}.ply'
        pc.export(out_name)
        print(f"Gespeichert unter: {out_name}")