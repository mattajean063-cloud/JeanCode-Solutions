from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "jeancode_solutions_secret_key"

@app.route("/")
def home():
    context = {
        "marca": "JeanCode Solutions",
        "titulo_pagina": "JeanCode Solutions | Páginas Web, E-commerce y Menús QR",
        "email_contacto": "soyjean063@gmail.com",
        "whatsapp_num": "+502 46511325",
        "whatsapp_clean": "50246511325",
        "categorias": [
            {
                "id": "menus",
                "nombre": "Menús y Catálogos QR Digitales",
                "icono": "fa-qrcode",
                "servicios": [
                    {
                        "id_modal": "modal_menu_visual",
                        "titulo": "Menú QR Digital (Visual)",
                        "precio": "Q450",
                        "mensualidad": "sin mensualidad",
                        "imagen": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=800&q=80",
                        "descripcion": "Menú interactivo y elegante para restaurantes, cafeterías o cevicherías. El cliente lo abre escaneando el QR desde su propio teléfono.",
                        "caracteristicas": ["100% adaptable a cualquier celular", "Fotografías HD por platillo y categorías", "Sin costos mensuales ni límites de escaneo"],
                        "ejemplo": "El cliente llega a la mesa, escanea el código con su celular y explora la carta digital con fotos, precios e ingredientes sin descargar apps.",
                        "demostracion": "Buscador de platillos instantáneo, filtro por categoría y opción de modo oscuro/claro."
                    },
                    {
                        "id_modal": "modal_menu_wp",
                        "titulo": "Menú QR + Carrito a WhatsApp",
                        "precio": "Q1,200",
                        "mensualidad": "Q50/mes",
                        "imagen": "https://images.unsplash.com/photo-1526367790999-0150786686a2?auto=format&fit=crop&w=800&q=80",
                        "descripcion": "Agiliza comandas y pedidos a domicilio. El cliente arma su consumo en pantalla y lo envía formateado directamente a tu WhatsApp.",
                        "caracteristicas": ["Carrito de compras interactivo", "Notas personalizadas (ej. Sin cebolla)", "Cálculo automático del total"],
                        "ejemplo": "El cliente elige 2 hamburguesas y una bebida en su celular, agrega detalles y presiona 'Enviar Pedido'. La orden llega limpia a tu chat.",
                        "demostracion": "Módulo interactivo con suma automática y desglose de cuenta en tiempo real."
                    },
                    {
                        "id_modal": "modal_menu_full",
                        "titulo": "Sistema de Pedidos Digital",
                        "precio": "Q1,700",
                        "mensualidad": "Q150/mes",
                        "imagen": "https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&w=800&q=80",
                        "descripcion": "Plataforma web con panel para ver pedidos en tiempo real desde cualquier teléfono, tablet o laptop que ya tengas.",
                        "caracteristicas": ["Panel de recepción de pedidos web", "Control de estados (Pendiente, En Preparación, Listo)", "Panel para cambiar precios al instante"],
                        "ejemplo": "Revisas las órdenes en tu propio celular o computadora en tiempo real. Puedes ocultar platillos agotados con un solo toque.",
                        "demostracion": "Panel administrativo para control total sin depender de equipos o licencias raras."
                    }
                ]
            },
            {
                "id": "ecommerce",
                "nombre": "Tiendas en Línea (E-commerce)",
                "icono": "fa-shopping-cart",
                "servicios": [
                    {
                        "id_modal": "modal_ecom_basic",
                        "titulo": "Tienda E-commerce Express",
                        "precio": "Q1,800",
                        "mensualidad": "Q200/mes",
                        "imagen": "https://images.unsplash.com/photo-1472851294608-062f824d29cc?auto=format&fit=crop&w=800&q=80",
                        "descripcion": "Catálogo de productos moderno para vender ropa, calzado, tecnología o accesorios por internet.",
                        "caracteristicas": ["Hasta 30 productos con variantes (Talla, Color)", "Carrito de compra interactivo", "Pedidos directos a tu WhatsApp"],
                        "ejemplo": "Tus clientes revisan los artículos desde su celular, eligen opciones y envían la solicitud de compra a tu WhatsApp.",
                        "demostracion": "Filtros de búsqueda rápida, galería de imágenes y botón directo de compra."
                    },
                    {
                        "id_modal": "modal_ecom_adv",
                        "titulo": "Tienda E-commerce PRO (Cobro Visa)",
                        "precio": "Q3,500",
                        "mensualidad": "Q250/mes",
                        "imagen": "https://images.unsplash.com/photo-1563013544-824ae1b704d3?auto=format&fit=crop&w=800&q=80",
                        "descripcion": "Plataforma completa con cobros en línea automatizados con tarjetas de crédito/débito y control de inventario.",
                        "caracteristicas": ["Catálogo de productos ilimitado", "Pasarela de pagos Visa/Mastercard", "Descuento automático de stock"],
                        "ejemplo": "El usuario paga directamente con su tarjeta en la web, el sistema valida la transacción y descuenta la mercancía del inventario.",
                        "demostracion": "Panel de control financiero para ver tus ventas e ingresos por día o mes."
                    }
                ]
            },
            {
                "id": "web",
                "nombre": "Páginas Web Profesionales",
                "icono": "fa-globe",
                "servicios": [
                    {
                        "id_modal": "modal_landing",
                        "titulo": "Landing Page Comercial",
                        "precio": "Q950",
                        "mensualidad": "Sin mensualidad",
                        "imagen": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
                        "descripcion": "Página de venta directa enfocada en captar prospectos y clientes mediante anuncios de redes sociales.",
                        "caracteristicas": ["Diseño de impacto centrado en ventas", "Muestra de servicios y testimonios", "Botonera directa de WhatsApp y llamadas"],
                        "ejemplo": "Perfecto para clínicas, talleres, servicios profesionales o consultorías que buscan cotizaciones constantes.",
                        "demostracion": "Estructura ligera optimizada para cargar en menos de 2 segundos en móviles."
                    },
                    {
                        "id_modal": "modal_corp",
                        "titulo": "Sitio Web Corporativo Enterprise",
                        "precio": "Q1,500",
                        "mensualidad": "Q250/mes",
                        "imagen": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80",
                        "descripcion": "Sitio web multi-página para proyectar prestigio, profesionalismo y presencia en búsquedas de Google.",
                        "caracteristicas": ["Hasta 6 secciones interactivas", "Formularios de cotización pro", "Posicionamiento SEO básico en Google"],
                        "ejemplo": "Ideal para empresas, colegios, constructoras o firmas que necesitan enviar propuestas corporativas sólidas.",
                        "demostracion": "Diseño empresarial con mapa de localización y secciones detalladas de servicios."
                    }
                ]
            },
            {
                "id": "pos",
                "nombre": "Sistemas Web de Control de Ventas (POS)",
                "icono": "fa-cash-register",
                "servicios": [
                    {
                        "id_modal": "modal_pos_cloud",
                        "titulo": "Sistema Web de Ventas y Caja",
                        "precio": "Q3,200",
                        "mensualidad": "Q350/mes",
                        "imagen": "https://images.unsplash.com/photo-1556740758-90de374c12ad?auto=format&fit=crop&w=800&q=80",
                        "descripcion": "Software 100% web para llevar el control de inventario, registro de ventas y caja desde tu teléfono o laptop actual.",
                        "caracteristicas": ["Funciona en cualquier dispositivo con navegador", "Control de stock de productos", "Reportes de ganancias diarias y mensuales"],
                        "ejemplo": "Abre la plataforma desde tu teléfono o laptop, registra tus ventas del día y obtén el cierre de caja sin pagar ningún equipo físico extra.",
                        "demostracion": "Reportes estadísticos de productos más vendidos y alerta de inventario bajo."
                    }
                ]
            }
        ],
        "faqs": [
            {"p": "¿Necesito comprar algún equipo, monitor o impresora?", "r": "¡No! Todos nuestros desarrollos son 100% software web. Funcionan perfectamente en cualquier teléfono, tablet o laptop que ya tengas."},
            {"p": "¿En cuánto tiempo entregan mi proyecto?", "r": "Los proyectos pequeños (Menús QR y Landing Pages) se entregan en 3 a 5 días hábiles. Las tiendas online o sistemas avanzados en 7 a 12 días hábiles."},
            {"p": "¿Tengo que pagar mensualidades?", "r": "Depende del tipo de proyecto. Las landing pages y menús QR básicos son de pago único sin comisiones. Sin embargo, los sistemas avanzados, tiendas en línea o plataformas que requieren servidores dedicados, bases de datos en la nube o soporte continuo cuentan con una tarifa de mantenimiento mensual."}
        ]
    }
    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
