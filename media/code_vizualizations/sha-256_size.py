import matplotlib.pyplot as plt

def visualize_large_number():
    grains_on_earth = 7.5e18
    two_to_255 = 2 ** 255
    
    earths_needed = two_to_255 / grains_on_earth
    
    fig, ax = plt.subplots(figsize=(10,6))
    
    # Bar for grains on one Earth
    ax.barh('One Earth', grains_on_earth, color='blue', label=f'Grains on One Earth: {grains_on_earth:.2e}')
    
    # Bar for 2^255
    ax.barh('2^255', two_to_255, color='red', label=f'2^255: {two_to_255:.2e}')
    
    ax.set_xscale('log')
    ax.set_xlabel('Number of Grains of Sand (Log Scale)')
    ax.set_title(f'Visualizing 2^255: Equivalent to the grains of sand on {earths_needed:.2e} Earths!')
    ax.legend()
    
    plt.tight_layout()
    plt.show()

visualize_large_number()
