class Integracion:

    def __init__(self):
        self.lim_inf = float(input('\nColoque el limite inferior: '))
        self.lim_sup = float(input('Coloque el limite superior: ')) 
        self.num_segments = int(input('Coloque el numero de segmentos: ')) 
        self.size_segments = (self.lim_sup-self.lim_inf)/self.num_segments 
        
    def vals_x(self):
        counter = self.lim_inf
        x_vals = [self.lim_inf]

        for _ in range(self.num_segments):
            x_vals.append(counter+self.size_segments)
            counter += self.size_segments
        
        return x_vals
    
    def funcion(self,x):
        return 0.2+25*x-200*(x**2)+675*(x**3)-900*(x**4)+400*(x**5) #Reemplazar aquí por la función a evaluar
    
    def y_vals(self):
        return [self.funcion(self.vals_x()[i]) for i in range(len(self.vals_x()))]
    
    def trapecio(self):
        suma = 0
        for i in range(1,len(self.y_vals())-1):
            suma += self.y_vals()[i]
        
        integral = ((self.lim_sup-self.lim_inf)*(self.y_vals()[0]+(2*suma)+self.y_vals()[self.num_segments]))/(2*self.num_segments)

        return f'La integral por la regla del trapecio con {self.num_segments} segmentos es igual a {integral}'
    
    def simpson_un_tercio(self):
        sum_pair = 0
        sum_odd = 0

        for i in range(1,len(self.y_vals())-1):
            if i%2 != 0:
                sum_odd += self.y_vals()[i]
            else:
                sum_pair += self.y_vals()[i]
        
        integral = ((self.lim_sup-self.lim_inf)*(self.y_vals()[0]+(4*sum_odd)+(2*sum_pair)+self.y_vals()[self.num_segments]))/(3*self.num_segments)

        return f'La integral por la regla de Simpson 1/3 con {self.num_segments} segmentos es igual a {integral}'
    
    def simpson_tres_octavos(self):
        sum1 = 0
        sum2 = 0
        sum3 = 0

        for i in range(1,len(self.y_vals())-1,3):
            sum1 += self.y_vals()[i]

        for i in range(2,len(self.y_vals())-1,3):
            sum2 += self.y_vals()[i]

        for i in range(3,len(self.y_vals())-1,3):
            sum3 += self.y_vals()[i]

        integral = ((3*(self.lim_sup-self.lim_inf))*(self.y_vals()[0]+(3*sum1)+(3*sum2)+(2*sum2)+self.y_vals()[self.num_segments]))/(8*self.num_segments)

        return f'La integral por la regla de Simpson 3/8 con {self.num_segments} segmentos es igual a {integral}'
    
    def segmentos_desiguales(self):
        segments = []

        for i in range(self.num_segments):
            segments.append(float(input(f'Coloque el tamaño del segmento {i+1}: ')))

        integral = 0

        for i in range(1,len(self.y_vals())):
            integral += segments[i-1]*(self.y_vals()[i]+self.y_vals()[i])/2

        return f'La integral por la regla del trapecio con segmentos desiguales es igual a {integral}'