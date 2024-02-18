import justpy as jp


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode="left", bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes='fit')
        qList = jp.QList(a=scroller)
        a_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=qList, text="Home", href='/', classes=a_classes)
        jp.Br(a=qList)
        jp.A(a=qList, text="About", href='/about', classes=a_classes)
        jp.Br(a=qList)
        jp.A(a=qList, text="Dictionary", href='/dictionary', classes=a_classes)
        jp.Br(a=qList)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu",
                click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='Instant Dictionary')

        container = jp.QPageContainer(a=layout)

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

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
