from guardrails import Guard

name_guard = Guard.fetch_guard(name="comp-toxic")

validation_outcome = name_guard.validate("Hello have a nice day. this is going good")
print(validation_outcome)