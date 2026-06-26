import trimesh
import numpy as np
import os

ply_path = "../../output/test/tsdf-rgbd.ply"
if not os.path.exists(ply_path):
    print(f"Fehler: {ply_path} nicht gefunden!")
    exit()

print("Lade Mesh...")
mesh = trimesh.load(ply_path, process=False)

points = np.asarray(mesh.vertices)
faces = np.asarray(mesh.faces)
colors = np.asarray(mesh.visual.vertex_colors[:, :3])
normals = np.asarray(mesh.vertex_normals)

print(f"Mesh geladen: {len(points)} Punkte.")

total_size = (mesh.bounds[1] - mesh.bounds[0]).max()
centers = (mesh.bounds[1] + mesh.bounds[0]) / 2
points = (points - centers) / total_size

n_points = len(points)
pose = np.zeros(72)
betas = np.zeros(10)
trans = np.zeros(3)
canon_pose = points.copy()
labels = np.zeros(n_points, dtype=np.int32)
coap_body_part = np.zeros(n_points, dtype=np.int32)

# Beispiel: 1 (Body), 3 (T-Shirt), 8 (Hose), 10 (Schuhe), 12 (Haare)
garments = np.zeros(18)
gesuchte_kleidung = [1, 3, 8, 10, 12]
for k in gesuchte_kleidung:
    garments[k] = 1

out_file = "my_scan.npz"
np.savez(
    out_file,
    points=points,
    faces=faces,
    colors=colors,
    normals=normals,
    scale=1.0/total_size,
    pose=pose,
    betas=betas,
    trans=trans,
    canon_pose=canon_pose,
    labels=labels,
    coap_body_part=coap_body_part,
    garments=garments,
    centers=centers
)
print(f"Erfolgreich gespeichert als {out_file}!")