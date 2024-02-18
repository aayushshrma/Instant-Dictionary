import justpy as jp
from webapp import layout
from webapp import page


class Home(page.Page):
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Welcome to Instant-Dictionary, where language meets convenience.
                Our web application is designed to make accessing definitions and expanding your vocabulary easier than ever 
                before. Whether you're a student looking to enhance your understanding of academic texts, a professional 
                seeking precision in your writing, or simply someone curious about the nuances of language, our instant 
                dictionary is here to serve you.
                """, classes='text-lg')

        return wp

