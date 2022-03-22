# Used Lambda to define anonymous Function and Map to generate a list of square of 1 To 20
result=list(map((lambda a: a*a),range(1,21)))
print(result)