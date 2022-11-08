T = int(input())
for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    a_company_cost = P * W
    b_company_cost = Q
    if W > R:
        b_company_cost += (W - R) * S
    if a_company_cost < b_company_cost:
        print("#" + str(t), a_company_cost)
    else:
        print("#" + str(t), b_company_cost)
