import math
import matplotlib.pyplot as plt

G = 6.673 * (10 ** (-11))
DRAWING_SCALE = 10**-5
DRAWING_SCREEN_OFFSET = (800, 500)
def get_gravitational_force(m1, m2, d):
    return G*m1*m2*10**-6/d**2 * (-1 if d < 0 else 1) ### unit adjustment: length in km

class Object:
    def __init__(self, name:str, mass, radius, init_pos:tuple, init_vec:tuple, init_accel:tuple=(0,0)):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.pos = list(init_pos)
        self.vec = list(init_vec)
        self.accel = list(init_accel)
    def update(self):
        self.vec[0] += self.accel[0]
        self.vec[1] += self.accel[1]
        self.pos[0] += self.vec[0]
        self.pos[1] += self.vec[1]
    def _calculate_distance_from(self, object):
        distance_vec = (object.pos[0] - self.pos[0], object.pos[1] - self.pos[1]) ### direction: from 'self' to 'object'
        distance = int(math.sqrt(distance_vec[0]**2 + distance_vec[1]**2))  ### Use integer part only
        if distance <= (self.radius + object.radius):
            print("Collision between %s and %s!" % (self.name, object.name))
            plt.show()
            exit(1)
        return distance, distance_vec
    def estimate_gravitational_force_from(self, object):
        '''
        Estimate gravitation force(=acceleration) from the given 'object' and update the self.accel value accordingly.
        The updated self.accel value shall be applied to the kinetic status of the instance when self.update() is invoked.
        :param object: Target Object instance to estimate gravitational force from.
        :return: None
        '''
        if type(object) is not Object:
            raise TypeError(object)
        distance, distance_vec = self._calculate_distance_from(object)
        force_vec = [get_gravitational_force(self.mass, object.mass, dv) for dv in distance_vec]
        self.accel = [force/self.mass for force in force_vec]
    def draw(self):
        plt.scatter(self.pos[0], self.pos[1])
        print(f'{self.name}: {self.pos[0]}, {self.pos[1]}')


if __name__ == "__main__":
    '''
    Units
    Mass: kg
    Length: km
    Speed: km/s
    Acceleration: km/s^2
    Time: second
    Force: Newton
    '''
    earth = Object("Earth", 5.98*10**24, 6.38*10**3, (8000, 0), (0, 0))
    asteroid = Object("Asteroid", 2*10**5, 50, (0, 10000), (0, 0))

    for _ in range(50):
        #force_to_earth = earth.estimate_gravitational_force_from(asteroid)
        force_to_asteroid = asteroid.estimate_gravitational_force_from(earth)
        #earth.update()
        asteroid.update()
        #earth.draw()
        asteroid.draw()

    plt.show()

    exit("\nSimulation ends.")