from guardrails import Guard, OnFailAction
from guardrails.hub import (
    BertToxic,
    CompetitorCheck
)

guard = Guard(name="comp-toxic").use_many(
    BertToxic(
        threshold=0.5,
        validation_method="sentence",
        on_fail=OnFailAction.EXCEPTION
    ),
    CompetitorCheck(
        competitors=["Apple", "Microsoft", "Google"]
    )
)

# guard.validate("Shut the hell up, we are going to the apple event today.")
# print(guard.validate("Hello have a nice day. this is going good."))