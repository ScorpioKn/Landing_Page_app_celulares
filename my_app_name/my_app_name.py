import reflex as rx

def index() -> rx.Component:
    return rx.container(
        #boton para cambiar el tema
        rx.color_mode.button(position="top-right"),
        
        rx.heading("!Gabriel's Tech World", size="9",color="white"),
        rx.hstack(
            rx.vstack(
                rx.text(
                "¡Gabriel's Tech World ofrece una gran variedad de celulares de alta gama para el gusto del cliente, con diferentes modelos y colores.",
                size="5", color="white"
            ),
            rx.hstack(
                    rx.link(
                        rx.button("Registrate aqui!",background="white",color="black"),
                        href="https://forms.gle/CskNNLMQtoPHVrVU9",
                        is_external=True,
                    ),
                    
                    rx.link(
                        rx.button(rx.icon(tag="instagram"),background="white",color="black"),
                        href="https://instagram.com",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button(rx.icon(tag="facebook"),background="white",color="black"),
                        href="https://www.facebook.com/",
                        is_external=True,
                    ),
                    rx.image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ--Z5jikTFZmETDyNbBFv_m2QzmdKxtrgNMQ&s"),
                ),
            ),
        
            spacing="9",
            justify="center",
            min_height="85vh",
        ),
        rx.vstack(
             rx.text(
                "modelos",
                size="9", color="white"
            ),
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Samsumg", value="tab1",color="white"),
                    rx.tabs.trigger("Iphone", value="tab2",color="white"),
                    rx.tabs.trigger("Realme", value="tab3",color="white"),
                    rx.tabs.trigger("Poco", value="tab4",color="white"),
                    rx.tabs.trigger("ZTE", value="tab5",color="white"),
                    rx.tabs.trigger("Huawei", value="tab6",color="white"),
                ),
                rx.tabs.content(
                    rx.image(src="https://rukminim2.flixcart.com/image/850/1000/xif0q/cases-covers/back-cover/g/l/b/ice-sams23ultra-clear-golden-sand-original-imah6gzcgs3djkmt.jpeg?q=20&crop=false"),
                    rx.image(src="https://http2.mlstatic.com/D_NQ_NP_942058-MLU78015452537_072024-O.webp"),
                    rx.image(src="https://http2.mlstatic.com/D_NQ_NP_656379-MLU74071993014_012024-O.webp"),
                    rx.image(src="https://assets.spares.nu/products/gallery/660120071D_Std2pi-LGAR6es2Mnn0mc.jpg"),
                    value="tab1",
                ),
                rx.tabs.content(
                    rx.image(src="https://pe.tiendasishop.com/cdn/shop/files/IMG-12496118_71065b39-c7c6-4861-b811-7c0ea6f9c884.jpg?v=1722624954"),
                    rx.image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQvIbCQZvWT0GE0Z54WifexlopSh87slVn-g&s"),
                    rx.image(src="https://promart.vteximg.com.br/arquivos/ids/5628813-1000-1000/imageUrl_1.jpg?v=637868558616030000"),
                    rx.image(src="https://www.entel.pe/wp-content/uploads/2021/11/ficha_especificaciones_iphone-13.jpg"),
                    value="tab2",
                ),
                rx.tabs.content(
                    rx.image(src="https://imagedelivery.net/4fYuQyy-r8_rpBpcY7lH_A/falabellaPE/133102207_02/w=800,h=800,fit=pad"),
                    rx.image(src="https://pe.celulares.com/fotos/realme-gt-5g-89980-g-alt.jpg"),
                    rx.image(src="https://http2.mlstatic.com/D_NQ_NP_938747-MLU79001710057_092024-O.webp"),
                    rx.image(src="https://movilpro.com.pe/products/images/celular-realme-c53-negro-black-movilpro-1725035491712.webp"),
                    value="tab3",
                ),
                rx.tabs.content(
                    rx.image(src="https://http2.mlstatic.com/D_NQ_NP_853157-MLA77242800681_062024-O.webp"),
                    rx.image(src="https://mercury.vtexassets.com/arquivos/ids/11948850/637915258978988583.jpg?v=638123849964730000"),
                    rx.image(src="https://oechsle.vteximg.com.br/arquivos/ids/16893519-1000-1000/image-fa221dabebed498fa74df870af5c8412.jpg?v=638364880652200000"),
                    rx.image(src="https://m.media-amazon.com/images/I/51qXb8txLIL._AC_SL1000_.jpg"),
                    value="tab4",
                ),
                rx.tabs.content(
                    rx.image(src="https://ofertec.pe/cdn/shop/files/ZTEA52020_4_1.jpg?v=1711754209"),
                    rx.image(src="https://imagedelivery.net/4fYuQyy-r8_rpBpcY7lH_A/falabellaPE/129901491_1/w=800,h=800,fit=pad"),
                    rx.image(src="https://plazavea.vteximg.com.br/arquivos/ids/29148899-512-512/20421953-4.jpg"),
                    rx.image(src="https://carsaperupoc.vtexassets.com/arquivos/ids/160094/VISTAS_V50-Vita-negro-.png?v=638517775683330000"),
                    value="tab5",
                  ),  
                  rx.tabs.content(
                    rx.image(src="https://tecno-sfera.com/wp-content/uploads/2024/07/Huawei-nova-Y90-Black-6.jpeg"),
                    rx.image(src="https://oechsle.vteximg.com.br/arquivos/ids/2755218-1000-1000/image-eeefc34e314c49c59820093283ef8361.jpg?v=637494940331370000"),
                    rx.image(src="https://http2.mlstatic.com/D_NQ_NP_2X_855771-MCR75370604933_032024-T.webp"),
                    rx.image(src="https://tecno-sfera.com/wp-content/uploads/2024/07/650_1200.jpeg"),
                    value="tab6",
                  ),  
            ),
            
            margin_top="-270px"
        ), 
        bg="orange"
    ),


app = rx.App()
app.add_page(index)
