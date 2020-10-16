#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:15:26 2020

@author: mateo
"""

def inicio_reaccion(codigo: str, hora_terminacion: int, minuto_terminacion: int,duracion_horas:int, duracion_minutos:int, duracion_segundos:int) -> str:
    
    hora_terminacion_segundos = hora_terminacion*3600
    minuto_terminacion_segundos = minuto_terminacion*60
    terminacion_total_segundos = hora_terminacion_segundos+minuto_terminacion_segundos
    
    
    duracion_horas_segundos= duracion_horas*3600
    duracion_minutos_segundos= duracion_minutos*60
    duracion_total_segundos = duracion_horas_segundos+duracion_minutos_segundos+duracion_segundos
    
    hora_a_iniciar= terminacion_total_segundos - duracion_total_segundos
    
    hora=(hora_a_iniciar/3600) # parte entera de hora es la hora, y la parte decimal son los minutos
    minutos= round((abs(hora)-abs(int(hora)))*(60),2)  #parte decimal de hora (minutos) * 60 para pasarlo a minutos           
    segundos= (abs(minutos)-abs(int(minutos)))*60  # parte decimal de minutos (segundos)*60 para pasar a segundos
    
    segundos=round(segundos)
    segundos=str(int(segundos)).zfill(2)
    hora=int(hora)
    minutos=int(minutos)
    hora=str(hora)
    minutos=str(minutos).zfill(2)
    return "La reacción {} debe iniciarse a las {} horas, {} minutos con {} segundos para que esté lista en en el momento requerido".format(codigo,hora,minutos,segundos)
print(inicio_reaccion("001", 16, 30, 7, 24, 58))