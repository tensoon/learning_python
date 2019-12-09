prem_ship = 125.00

def sh_cost(weight):
  if weight <= 2:
    cost = weight * 1.50
  elif weight <= 6:
    cost = weight * 3.00
  elif weight <= 10:
    cost = weight * 4.00
  else:
    cost = weight * 4.75
  return cost + 20


  
def sh_cost_dr(weight):
  if weight <= 2:
    cost = weight * 4.50
  elif weight <= 6:
    cost = weight * 9.00
  elif weight <= 10:
    cost = weight * 12.00
  else:
    cost = weight * 14.25
  return cost


def total_cost(weight):
  ground = sh_cost(weight)
  drone = sh_cost_dr(weight)
  premium = prem_ship
  
  if ground < premium and ground < drone:
    method = "Standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "Premium ground"
    cost = premium
  else:
    method = "Drone"
    cost = drone
  print(f"The cheapest option available is ${cost} with {method} shipping.")
  
total_cost(452)