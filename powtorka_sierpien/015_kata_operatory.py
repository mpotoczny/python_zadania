def expression_matter(a, b, c):

    results_set = set()

    results_set.add( a*(b+c) )
    results_set.add( a+b+c )
    results_set.add( a*b*c )
    results_set.add( a+b*c )
    results_set.add( (a+b)*c )

    return max(results_set)

    # sprawdzę jak to działa
    # def expression_matter(a, b, c):
    #     return max(max(eval(f'{a}{op1}({b}{op2}{c})'), eval(f'({a}{op1}{b}){op2}{c}')) for op1 in '+*' for op2 in '+*')


print(expression_matter(1,2,3))