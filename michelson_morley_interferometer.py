import numpy as np


def draw_interferometer_table(axes, table_radius):
    from matplotlib.patches import Circle
    table = Circle((0, 0), radius=table_radius,
                   edgecolor='black', facecolor='white')
    axes.add_patch(table)
    return


def draw_beam_splitter(axes, table_radius, beam_splitter_angle):
    from matplotlib.patches import Rectangle

    beam_splitter_height = 0.005 * table_radius
    beam_splitter_width = 0.15 * table_radius
    beam_splitter = Rectangle((0, -0.5*beam_splitter_width),
                              beam_splitter_height, beam_splitter_width,
                              angle=np.degrees(beam_splitter_angle),
                               # rotation_point='center',
                              color='k')
    axes.add_patch(beam_splitter)
    return


def visualize_planar_interferometer(table_radius, beam_splitter_angle):
    import matplotlib
    import matplotlib.pyplot as plt

    # matplotlib.use('macosx')

    figure, axes = plt.subplots()

    # Check center
    # plt.plot([-0.1, 0.1, 0.1, -0.1],
    #          [-0.1, -0.1, 0.1, 0.1],
    #          color='blue')

    draw_interferometer_table(axes, table_radius)
    draw_beam_splitter(axes, table_radius, beam_splitter_angle)
    # draw_light_source(axes, table_radius, source_angular_position)
    # draw_mirrors(axes, table_radius, mirror_angular_positions)
    # draw_beams(axes, table_radius, source_angular_position, mirror_angular_positions)

    # Set axis limits to 10% larger than table
    white_space_factor = 0.1
    plot_limit_extreme = (1. + white_space_factor) * table_radius
    axes.set(xlim=[-plot_limit_extreme, plot_limit_extreme],
             ylim=[-plot_limit_extreme, plot_limit_extreme])

    # Set aspect ratio to 1 and turn off axes
    axes.set_aspect('equal')
    plt.axis('off')
    plt.show()

    return


def visualize_spatial_interferometer(table_radius, beam_splitter_angle):
    import vpython as vp

    scene = vp.canvas()
    scene.camera.pos = vp.vec(0, 2, 0)

    # Draw table
    table_thickness = 0.02 * table_radius
    table = vp.cylinder(pos=vp.vec(0, 0, 0), axis=vp.vec(0, table_thickness, 0),
                        radius=table_radius, color=vp.color.white)

    return


def visualize_michelson_morely_interferometer(number_of_dimensions):
    # Quantities common to both 2D and 3D
    table_radius = 10
    beam_splitter_angle = np.radians(45)

    if number_of_dimensions == 2:
        visualize_planar_interferometer(table_radius, beam_splitter_angle)

    elif number_of_dimensions == 3:
        visualize_spatial_interferometer(table_radius, beam_splitter_angle)

    else:
        raise ValueError("The number of dinensions must be 2 or 3")

    return


if __name__ == '__main__':
    visualize_michelson_morely_interferometer(2)
