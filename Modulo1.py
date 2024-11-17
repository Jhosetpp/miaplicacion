def gradoAPI(ge):
    #Calcula el grado API apartir del la gravedad específica
    #parámetros ge:gravedad específica del crudo
    #retorna la gravedad API calculada
    resultado_API=(141.5/ge)-131.5
    return resultado_API
def poes(a,h,porosidad,so,bo):
    resultado_poes=((43560*a*h*porosidad*so)/bo)/1000000
    return print("el poes calculado es" ,resultado_poes,"MBLS")