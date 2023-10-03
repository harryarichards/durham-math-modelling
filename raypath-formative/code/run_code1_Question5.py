import ray_IASP91_v1

ray = ray_IASP91_v1.Raytrace()

T, Delta = ray.trajectory(16.5, 'P', 0.1)
print("T=", T, " Delta=", Delta)

ray.plot_VpVs()

ray.plot_trajectory()
