from matplotlib import pyplot as plt

nombres = ["Procesados","Rechazados"]

ventana25 = plt.figure('Porcentaje de rechazo para relacion de tasas del 25%')
subplot25_k0 = ventana25.add_subplot(221)
k_0 = [10000, 2498]
subplot25_k0.pie(k_0, labels=nombres, autopct="%0.1f %%")
subplot25_k0.axis('equal')
subplot25_k0.set_title('Tamaño de cola = 0')

subplot25_k2 = ventana25.add_subplot(222)
k_2 = [10000, 120]
subplot25_k2.pie(k_2, labels=nombres, autopct="%0.1f %%")
subplot25_k2.axis('equal')
subplot25_k2.set_title('Tamaño de cola = 2')

subplot25_k5 = ventana25.add_subplot(223)
k_5 = [10000,2]
subplot25_k5.pie(k_5, labels=nombres, autopct="%0.1f %%")
subplot25_k5.axis('equal')
subplot25_k5.set_title('Tamaño de cola = 5')

#ventana25.savefig('images/denegacion_tasa25.0.png')

#-------------------------------------------------------------------------------

ventana50 = plt.figure('Porcentaje de rechazo para relacion de tasas del 50%')
subplot50_k0 = ventana50.add_subplot(221)
k_0 = [10000, 4924]
subplot50_k0.pie(k_0, labels=nombres, autopct="%0.1f %%")
subplot50_k0.axis('equal')
subplot50_k0.set_title('Tamaño de cola = 0')

subplot50_k2 = ventana50.add_subplot(222)
k_2 = [10000, 707]
subplot50_k2.pie(k_2, labels=nombres, autopct="%0.1f %%")
subplot50_k2.axis('equal')
subplot50_k2.set_title('Tamaño de cola = 2')

subplot50_k5 = ventana50.add_subplot(223)
k_5 = [10000, 84]
subplot50_k5.pie(k_5, labels=nombres, autopct="%0.1f %%")
subplot50_k5.axis('equal')
subplot50_k5.set_title('Tamaño de cola = 5')

subplot50_k10 = ventana50.add_subplot(224)
k_10 = [10000, 1]
subplot50_k10.pie(k_10, labels=['P.','Rechazados'], autopct="%0.1f %%")
subplot50_k10.axis("equal")
subplot50_k10.set_title('Tamaño de cola = 10')

#ventana50.savefig('images/denegacion_tasa50.0.png')

#-------------------------------------------------------------------------------
nombres=['P.','R.']

ventana75 = plt.figure('Porcentaje de rechazo para relacion de tasas del 75%')
subplot75_k0 = ventana75.add_subplot(231)
k_0 = [10000, 7715]
subplot75_k0.pie(k_0, labels=nombres, autopct="%0.1f %%")
subplot75_k0.axis('equal')
subplot75_k0.set_title('Tamaño cola = 0')

subplot75_k2 = ventana75.add_subplot(232)
k_2 = [10000, 1843]
subplot75_k2.pie(k_2, labels=nombres, autopct="%0.1f %%")
subplot75_k2.axis('equal')
subplot75_k2.set_title('Tamaño cola = 2')

subplot75_k5 = ventana75.add_subplot(233)
k_5 = [10000, 522]
subplot75_k5.pie(k_5, labels=nombres, autopct="%0.1f %%")
subplot75_k5.axis('equal')
subplot75_k5.set_title('Tamaño cola = 5')

subplot75_k10 = ventana75.add_subplot(234)
k_10 = [10000, 141]
subplot75_k10.pie(k_10, labels=nombres, autopct="%0.1f %%")
subplot75_k10.axis("equal")
subplot75_k10.set_title('Tamaño cola = 10')

subplot75_k50 = ventana75.add_subplot(235)
k_50 = [10000, 0]
subplot75_k50.pie(k_50, labels=nombres, autopct="%0.1f %%")
subplot75_k50.axis("equal")
subplot75_k50.set_title('Tamaño de cola = 50')

#ventana75.savefig('images/denegacion_tasa75.0.png')

#-------------------------------------------------------------------------------

ventana100 = plt.figure('Porcentaje de rechazo para relacion de tasas del 100%')
subplot100_k0 = ventana100.add_subplot(231)
k_0 = [10000, 9908]
subplot100_k0.pie(k_0, labels=nombres, autopct="%0.1f %%")
subplot100_k0.axis('equal')
subplot100_k0.set_title('Tamaño cola = 0')

subplot100_k2 = ventana100.add_subplot(232)
k_2 = [10000, 3052]
subplot100_k2.pie(k_2, labels=nombres, autopct="%0.1f %%")
subplot100_k2.axis('equal')
subplot100_k2.set_title('Tamaño cola = 2')

subplot100_k5 = ventana100.add_subplot(233)
k_5 = [10000, 1690]
subplot100_k5.pie(k_5, labels=nombres, autopct="%0.1f %%")
subplot100_k5.axis('equal')
subplot100_k5.set_title('Tamaño cola = 5')

subplot100_k10 = ventana100.add_subplot(234)
k_10 = [10000, 853]
subplot100_k10.pie(k_10, labels=nombres, autopct="%0.1f %%")
subplot100_k10.axis("equal")
subplot100_k10.set_title('Tamaño cola = 10')

subplot100_k50 = ventana100.add_subplot(235)
k_50 = [10000, 69]
subplot100_k50.pie(k_50, labels=nombres, autopct="%0.1f %%")
subplot100_k50.axis("equal")
subplot100_k50.set_title('Tamaño cola = 50')

#ventana100.savefig('images/denegacion_tasa100.0.png')

#-------------------------------------------------------------------------------

ventana125 = plt.figure('Porcentaje de rechazo para relacion de tasas del 125%')
subplot125_k0 = ventana125.add_subplot(231)
k_0 = [10000, 12320]
subplot125_k0.pie(k_0, labels=nombres, autopct="%0.1f %%")
subplot125_k0.axis('equal')
subplot125_k0.set_title('Tamaño cola = 0')

subplot125_k2 = ventana125.add_subplot(232)
k_2 = [10000, 5150]
subplot125_k2.pie(k_2, labels=nombres, autopct="%0.1f %%")
subplot125_k2.axis('equal')
subplot125_k2.set_title('Tamaño cola = 2')

subplot125_k5 = ventana125.add_subplot(233)
k_5 = [10000, 3221]
subplot125_k5.pie(k_5, labels=nombres, autopct="%0.1f %%")
subplot125_k5.axis('equal')
subplot125_k5.set_title('Tamaño cola = 5')

subplot125_k10 = ventana125.add_subplot(234)
k_10 = [10000, 2686]
subplot125_k10.pie(k_10, labels=nombres, autopct="%0.1f %%")
subplot125_k10.axis("equal")
subplot125_k10.set_title('Tamaño cola = 10')

subplot125_k50 = ventana125.add_subplot(235)
k_50 = [10000, 2233]
subplot125_k50.pie(k_50, labels=nombres, autopct="%0.1f %%")
subplot125_k50.axis("equal")
subplot125_k50.set_title('Tamaño cola = 50')
plt.show()