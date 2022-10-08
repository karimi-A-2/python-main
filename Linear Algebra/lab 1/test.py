import matplotlib

matplotlib.use('macosx')
import matplotlib.pyplot

data = (3, 6, 9, 12, 15)
fig, simple_chart = matplotlib.pyplot.subplots()
simple_chart.plot(data)
matplotlib.pyplot.show()

# ['GTK3Agg', 'GTK3Cairo', 'GTK4Agg', 'GTK4Cairo',
# 'MacOSX', 'nbAgg', 'QtAgg', 'QtCairo', 'Qt5Agg',
# 'Qt5Cairo', 'TkAgg', 'TkCairo', 'WebAgg', 'WX',
# 'WXAgg', 'WXCairo', 'agg', 'cairo', 'pdf', 'pgf',
# 'ps', 'svg', 'template']
