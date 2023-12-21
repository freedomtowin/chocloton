# NOT USED

# def exp_average_breed(parameters):

#     N = successful_mutations.shape[1]
#     if N<=1:
#         return 0
    
#     n_breed_combos = (N+1)*N//2 - N
#     breed_list = np.zeros((successful_mutations.shape[0], n_breed_combos))
#     count = 0
#     for i in range(successful_mutations.shape[1]):
#         for j in range(successful_mutations.shape[1]):
#             if i<=j:
#                 continue
#             breed_list[:,count] =0.5*successful_mutations[:,i]+0.5*successful_mutations[:,j]
#             count+=1

#     return breed_list