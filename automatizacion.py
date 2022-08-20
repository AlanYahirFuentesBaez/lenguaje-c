from asyncio.windows_events import NULL
import sys

def generaUrlBusqueda(terminoBusqueda,ordenamiento,cantidadItems ):
    terminoBusqueda=sys.argv[1] 
    ordenamiento=sys.argv[2] 
    cantidadItems=sys.argv[3]

    url = '/bsq/'+ terminoBusqueda + '?orderBy='+ordenamiento+'&pageSize='+cantidadItems

    return url

#El primer argumento debe ser el ALT y el SEGUNDO el nombre de la imagen
#https://dp-imagenes.s3.amazonaws.com/wcsstore/DpstreetStorefrontAssetStore/images/banner-dps-home/desk
#https://dp-imagenes.s3.amazonaws.com/wcsstore/DpstreetStorefrontAssetStore/images/banner-dps-home/mobile
#El tercer argumento debe ser la url del href

#https://dp-imagenes.s3.amazonaws.com/wcsstore/DpstreetStorefrontAssetStore/bannersMarcas/2022/bannersCategories/ofertasDPS/desk/style-week.jpg

if(len(sys.argv) == 1):
    print("Orden de parámetros: alt , imgUrl , href , tipoBanner")
    print("Ejemplo: py banner.py PUMA-MAYZE dpstreet.jpg /marcas-dpstreet/adidas-marcas-dpstreet 1 > banner.html")
elif(sys.argv[4] == "1"):
    #banner del home
    alt=sys.argv[1]    
    imgUrl=sys.argv[2]    
    href=sys.argv[3]

    codigo='<div class="only-desktop">\n\t<a href="' + href +' " class="bloque_link">\n\t\t<img alt="DPSTREET-'+ alt + '"  src="https://dp-imagenes.s3.amazonaws.com/wcsstore/DpstreetStorefrontAssetStore/images/banner-dps-home/desk' + imgUrl +'.jpg">\n\t</a>\n</div>\n\n<div class="only-mobile">\n\t<a href="' + href +' ">\n\t\t<img alt="DPSTREET-' + alt +' " class="lazyload" src="https://dp-imagenes.s3.amazonaws.com/wcsstore/DpstreetStorefrontAssetStore/images/banner-dps-home/mobile'+ imgUrl +'.jpg">\n\t</a>\n</div>'
    print(codigo)



elif(sys.argv[4] == "3"):
    #banner de categorias

    alt=sys.argv[1]    
    imgUrlDesk=sys.argv[2]
    imgUrlMobile=sys.argv[3]   

    codigo='<div id="atraction">\n\t<div class="only-desktop">\n\t\t<img alt="DPSTREET-'+ alt + '" class="lazyload" src="https://dp-imagenes.s3.amazonaws.com/wcsstore/DpstreetStorefrontAssetStore/bannersMarcas/2022' + imgUrlDesk +'.jpg">\n\t</div>\n\t<div class="only-mobile">\n\t\t<img alt="DPSTREET-' + alt +' "class="lazyload" src="https://dp-imagenes.s3.amazonaws.com/wcsstore/DpstreetStorefrontAssetStore/bannersMarcas/2022' + imgUrlMobile +'.jpg">\n\t</div>\n</div>'
    print(codigo)


elif(sys.argv[4] == "4"):
    #regla de busqueda
    bsq=sys.argv[1] 
    orderBy=sys.argv[2] 
    pageSize=sys.argv[3]
    codigo=generaUrlBusqueda(bsq,orderBy,pageSize)
    print("bsq orderBy pageSize")
    print("\t\t!!!Instrucciones: orderBy puede ser del 1 al 5 y pageSize, 24 0 36!!!")
    print("\t\t!!orderBy=4----------->Mayor Precio")
    print("\t\t!!orderBy=5----------->Más nuevo")
    #no olvidar contemplar %20
    print(codigo)


elif(sys.argv[5] == "2"):
    #banner de lp

    alt=sys.argv[1]    
    imgUrlDesk=sys.argv[2]
    imgUrlMobile=sys.argv[3]   
    href=sys.argv[4]

    
    codigo='<div class="only-desktop">\n\t<a href="' + href +' " class="bloque_link">\n\t\t<img alt="DPSTREET-'+ alt + '"  src="https://dp-imagenes.s3.amazonaws.com/wcsstore/DpstreetStorefrontAssetStore/images' + imgUrlDesk +'.jpg">\n\t</a>\n</div>\n\n<div class="only-mobile">\n\t<a href="' + href +' ">\n\t\t<img alt="DPSTREET-' + alt +' " class="lazyload" src="https://dp-imagenes.s3.amazonaws.com/wcsstore/DpstreetStorefrontAssetStore/images' + imgUrlMobile +'.jpg' +'">\n\t</a>\n</div>'
    print(codigo)
