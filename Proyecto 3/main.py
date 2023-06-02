from scipy.stats import binom, geom, poisson
import matplotlib.pyplot as plt
from statistics import median, mode
from numpy import mean, var

def getRandomData(distribution, size, n=100, bp=0.35, L=30, gp=0.08):
    if(distribution == 'binom'):
        return binom.rvs(n, bp, size=size)
    elif(distribution == 'geom'):
        return geom.rvs(gp,size = size)
    else:
        return poisson.rvs(L, size=size)

def distributionGraphics(distribution, n=100, bp=0.35, L=30, gp=0.08):
    distributions = { 
                     'binom':   ['Binomial', bp*n, n*bp*(1-bp)],
                     'geom':    ['Geomterica', 1/gp,  (1 - gp) / (gp**2)],
                     'poisson': ['Poisson', L, L]
                     }
    
    fig, ((bx1, bx2, bx3, bx4), (h1, h2, h3, h4)) = plt.subplots(2, 4, figsize=(12, 9))
    bx = [bx1, bx2, bx3, bx4]
    hists = [h1, h2, h3, h4]
    
    for i in range(2, 6):
        boxPlotGraphic =  bx[i - 2]
        histGraphic    =  hists[i - 2]
        
        data = getRandomData(distribution, pow(10, i), n=n, bp=bp, L=L, gp=gp)
        boxPlotGraphic.boxplot(data) 
        boxPlotGraphic.set_title(f'Muestra {distributions[distribution][0]} 10^{i}')
        histGraphic.hist(data, color="Red",bins = int(180/5))
        
        text = f'Mediana: {median(data)}\nModa: {mode(data)}\nMedia empirica: {round(mean(data), 2)}\nEsperanza teorica: {distributions[distribution][1]}\nVarianza empirica: {round(var(data), 2)}\nVarianza teorica: {distributions[distribution][2]}'
        boxPlotGraphic.text(0.04, 0.75, text, transform=boxPlotGraphic.transAxes, fontsize=6,
                 bbox=dict(facecolor='white', edgecolor='black', alpha=0.6),
                 ha='left')

    plt.tight_layout()
    plt.subplots_adjust(wspace=0.198)
    plt.get_current_fig_manager().window.state('zoomed')
    fig.canvas.manager.set_window_title(f"Distribucion {distributions[distribution][0]}")
    plt.show()

distributionGraphics('binom', n=100, bp=0.35)
distributionGraphics('geom', gp=0.08)
distributionGraphics('poisson', L=30)
