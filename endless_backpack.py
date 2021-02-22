def main():
    n, w = map(int, input().split())            # кол-во предметов, вместимость рюкзака
    objects = []
    for i in range(n):
        l, r = map(int, input().split())        # стоимость, вес
        couple = (l, r)
        objects.append(couple)

    objects = sorted(objects, key=lambda object: object[0]/object[1], reverse=True)
    total_cost = 0

    for obj in objects:
        if w - obj[1] >= 0:
            w -= obj[1]
            total_cost += obj[0]
        else:
            total_cost += obj[0] * (w / obj[1])
            w = 0
            break
    return total_cost


main()
