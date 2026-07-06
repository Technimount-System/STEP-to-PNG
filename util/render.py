import pyvista as pv

def render(mesh, camera_position, output_path, window_size=(1200, 900)):
    pl = pv.Plotter(off_screen=True, window_size=window_size)
    pl.set_background("white")
    pl.add_mesh(
        mesh,
        color="#949494",
        smooth_shading=False,
        specular=0.5,
        specular_power=15,
    )
    pl.add_mesh(
        mesh.extract_feature_edges(),
        color="black",
    )
    pl.add_light(pv.Light(position=(5, 5, 5),  light_type="scene light", intensity=0.8))
    pl.add_light(pv.Light(position=(-5, -3, 3), light_type="scene light", intensity=0.3))
    pl.camera_position = camera_position
    pl.reset_camera()
    pl.screenshot(output_path)
    pl.close()
    print(f"Saved → {output_path}")

def render_mesh_twice(mesh):
    render(mesh, camera_position="iso",   output_path="view_isometric.png")
    render(mesh, camera_position="xz",    output_path="view_front.png")