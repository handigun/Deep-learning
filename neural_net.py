from hw_utils import * 
import time
if __name__ == "__main__":
	din = 50
	dout = 2
	train_data, train_target, test_data, test_target = loaddata("MiniBooNE_PID.txt")
	train_data, test_data = normalize(train_data, test_data)
	#PART d1
	# start =  time.time()
	# arch_lst = [[din, dout], [din, 50, dout], [din, 50, 50, dout], [din, 50,50, 50, dout]]
	# best = testmodels(train_data, train_target, test_data, test_target, arch_lst, 'linear', 'softmax', [0.0], 30, 1000, 0.001, [0.0], [0.0], False, False, 0)
	# end = time.time()
	# print("Time taken", end - start)
	# #PART d2
	# start =  time.time()
	# arch_lst = [[din, 50, dout], [din, 500, dout], [din, 500, 300, dout], [din, 800, 500, 300, dout], [din, 800, 800, 500, 300, dout]]
	# best = testmodels(train_data, train_target, test_data, test_target, arch_lst, 'linear', 'softmax', [0.0], 30, 1000, 0.001, [0.0], [0.0], False, False, 0)
	# end = time.time()
	# print("Time taken", end - start)
	# # #PART e
	# start =  time.time()
	# best = testmodels(train_data, train_target, test_data, test_target, arch_lst, 'sigmoid', 'softmax', [0.0], 30, 1000, 0.001, [0.0], [0.0], False, False, 0)
	# end = time.time()
	# print("Time taken", end - start)
	# # #PART f
	# start =  time.time()
	# best = testmodels(train_data, train_target, test_data, test_target, arch_lst, 'relu', 'softmax', [0.0], 30, 1000, 5e-4, [0.0], [0.0], False, False, 0)
	# end = time.time()
	# print("Time taken", end - start)
	# # #PART g
	# start =  time.time()
	# arch_lst = [[din, 800, 500, 300, dout]]
	# best = testmodels(train_data, train_target, test_data, test_target, arch_lst, 'relu', 'softmax', [1e-7, 5e-7, 1e-6, 5e-6, 1e-5], 30, 1000, 5e-4, [0.0], [0.0], False, False, 0)
	# end = time.time()
	# print("Time taken", end - start)
	# # #PART h
	# start =  time.time()
	# best = testmodels(train_data, train_target, test_data, test_target, arch_lst, 'relu', 'softmax', [1e-7, 5e-7, 1e-6, 5e-6, 1e-5], 30, 1000, 5e-4, [0.0], [0.0], False, True, 0)
	# end = time.time()
	# print("Time taken", end - start)
	# best_coeff = best[1]
	# #part i
	# start =  time.time()
	# best = testmodels(train_data, train_target, test_data, test_target, arch_lst, 'relu', 'softmax', [5e-7], 100, 1000, 1e-5, [1e-5, 5e-5, 1e-4, 3e-4, 7e-4, 1e-3], [0.0], False, False, 0)
	# end = time.time()
	# print("Time taken", end - start)
	# #part j
	# start =  time.time()
	# best_prev = best
	# best = testmodels(train_data, train_target, test_data, test_target, arch_lst, 'relu', 'softmax', [ 5e-7], 50, 1000, 1e-5, [best_prev[2]], [0.99, 0.98, 0.95, 0.9, 0.85], True, False, 0)
	# end = time.time()
	# print("Time taken", end - start)
	# #part k
	# start =  time.time()
	# best_prev = best
	# #arch_lst = [[din, 800, 500, 300, dout]]
	# best = testmodels(train_data, train_target, test_data, test_target, arch_lst, 'relu', 'softmax', [best_coeff], 100, 1000, 1e-5, [best_prev[2]], [best_prev[3]], True, True, 0)
	# end = time.time()
	# print("Time taken", end - start)
	# #part l
	# arch_lst = [[din, 50, dout], [din, 500, dout], [din, 500, 300, dout], [din, 800, 500, 300, dout], [din, 800, 800, 500, 300, dout]]
	# best = testmodels(train_data, train_target, test_data, test_target, arch_lst, 'relu', 'softmax', [ 1e-7, 5e-7, 1e-6, 5e-6, 1e-5], 100, 1000, 1e-5, [1e-5, 5e-5, 1e-4], [0.99], True, True, 0)
	# end = time.time()
	# print("Time taken", end - start)
