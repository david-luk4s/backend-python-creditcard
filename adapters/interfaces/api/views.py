from jsonpickle import encode, decode

from adapters.interfaces.api.handle import API
from adapters.infrastructure.jwt.user import BaseJWT

from application.card import AppCard
from application.user import AuthSerializer
from application.auth import BaseAuth

app = API()

@app.route("/api/v1/credit-card/{id_card}")
def recovery_card(request: any, response: any, id_card: str) -> None:
    """This function ."""
    response.content_type = "application/json"

    if request.method != 'GET':
        response.text = encode({"error": "not allowed method"})
        return

    card = AppCard().detail_card(id_card)
    if card is None:
        response.text = encode({"message": "card not found"})
        response.status = "404 Not Found"
        return

    response.text = encode(card, unpicklable=False)


@app.route("/api/v1/credit-card")
def card(request: any, response: any) -> None:
    """This function ."""
    response.content_type = "application/json"
    app_card = AppCard(request.body)

    if request.method == 'POST':
        if not app_card.is_valid():
            response.text = encode({"error": "error data validation"})
            return

        app_card.process_card()
        app_card.save()

        response.text = encode(app_card.card, unpicklable=False)
        return


    elif request.method == 'GET':
        response.text = encode(app_card.list_cards(), unpicklable=False)
        return

@app.route("/api/v1/auth/token")
def generator_token(request: any, response: any) -> None:
    """This function ."""
    response.content_type = "application/json"

    if request.method != 'POST':
        response.text = encode({"error": "method not allowed"})
        return

    auth = BaseAuth(AuthSerializer(request.body))

    if auth.authenticate():
        bjwt = BaseJWT(auth.user)

        response.text = encode({"token": bjwt.generator_token()}, unpicklable=False)
        return

    response.text = encode({"message": "Unauthorized"}, unpicklable=False)
    response.status = '401 Unauthorized'

@app.route("/api/v1/auth/token/verify")
def verify_token(request: any, response: any) -> None:
    """This function ."""
    response.content_type = "application/json"

    if request.method != 'POST':
        response.status = '401 Unauthorized'
        response.text = encode({"error": "method not allowed"})
        return

    if request.body is None:
        response.status = '401 Unauthorized'
        response.text = encode({"error": "expected token"})
        return

    data = decode(request.body.decode())
    bjwt = BaseJWT.decode_token(data.get("token"))

    response.text = encode(bjwt, unpicklable=False)
    response.status = '202 OK'
    return 
