import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cartopy.crs as ccrs

def world_map_plotter(latitude, longitude):
    fig = plt.figure(figsize=(10, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.stock_img()

    ax.scatter(longitude, latitude, transform=ccrs.PlateCarree(), s=20, color='b')
    ax.set_title('ISS Trajectory on World Map')
    
    plt.show()
