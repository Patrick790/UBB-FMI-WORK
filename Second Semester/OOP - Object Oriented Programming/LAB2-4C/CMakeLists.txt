cmake_minimum_required(VERSION 3.22.1)
project(lab2_4agentie C)

set(CMAKE_C_STANDARD 11)

add_executable(lab2_4agentie main.c Oferta.c Oferta.h OfertaRepository.c OfertaRepository.h Service.c Service.h Vector.c Vector.h UI.c UI.h)
