import csv

def demand_function(quantity, time):
	return 100 - quantity + int((time/5))

def supply_function(time):
	#perfectly competitive market so set equal to margian cost. marginal cost will drop with time though thanks to technology advancements hence the -)
	return 50.00 - int((time/100))

def inverse_demand_function(price, time):
	return 100 + int((time/5)) - price

def inverse_supply_function(time):
	return 50.00 + int((time/100)) + int((time/5))

def equilibrium_quantity(time):
	#pass the value from this into the demand_function or supply_function to get equilirbium price
	return 50 + int((time/5)) + int((time/100)) 

ofilePosts = open('simulation_results.csv', 'w')
writerPosts = csv.writer(ofilePosts, delimiter=',')

writerPosts.writerow(['t', 'p', 'q', 'in equilibrium', 'p_e', 'q_e'])

initial_p = 32.05
max_price_update = 8.00

duration_of_simulation = 10

is_first = True
for t in range(0, duration_of_simulation):
	in_equilibrium = False
	if is_first == True:
		is_first = False
		p = initial_p

		q_e = equilibrium_quantity(t)
		p_e = demand_function(q_e, t)

		if p == p_e:
			in_equilibrium = True
			q = inverse_demand_function(p, t)
		elif p < p_e:
			q = inverse_supply_function(t)
		elif p > p_e:
			q = inverse_demand_function(p, t)
	else:
		if p_e != p or q_e != q:
			if abs(p_e - p) < max_price_update:
				in_equilibrium = True
				p = p_e
				q = inverse_demand_function(p, t)
			else:
				if p < p_e:
					p = p + max_price_update
					q = inverse_supply_function(t)
				else:
					p = p - max_price_update
					q = inverse_demand_function(p, t)
		else:
			in_equilibrium = True

		#Check if p_e and q_e have changed.
		if q_e != equilibrium_quantity(t):
			in_equilibrium = False
			q_e = equilibrium_quantity(t)
			p_e = demand_function(q_e, t)
	print("time: " + str(t))
	print("price:" + str(p))
	print("quantity:" + str(q))
	print("is in equilibrium: " + str(in_equilibrium))
	print('equilibrium price:' + str(p_e))
	print('equilibrium quantity: ' + str(q_e))
	print('--------------')
	writerPosts.writerow([t, p, q, in_equilibrium, p_e, q_e])



