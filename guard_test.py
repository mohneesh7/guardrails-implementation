from guardrails import Guard

name_guard = Guard.fetch_guard(name="comp-toxic")

validation_outcome = name_guard.validate("Hello have a nice day. this is going good I am on the way to buy an apple phone and return you dipshit.")
print(validation_outcome)