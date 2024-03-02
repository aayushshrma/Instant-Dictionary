import justpy as jp


class Api:
    """
    Handles requests at /api?w=word
    """

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        wp.html = word.title()
        return wp


jp.Route("/api", Api.serve)
jp.justpy()
