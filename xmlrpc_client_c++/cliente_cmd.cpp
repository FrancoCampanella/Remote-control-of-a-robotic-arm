
#include <iostream>
#include <stdlib.h>
#include <sstream>
using namespace std;
#include "XmlRpc.h"
using namespace XmlRpc;

int main(int argc, char* argv[])
{
    int port, i=0;
    float vel;
    try{

        XmlRpc::XmlRpcValue Args, sinArgs, unArg, dosArgs, resultado;

        while (i!=1){
            std::cout<<"================================================="
                   <<"\nIngrese la accion a realizar:"<<endl
                   <<"0-Para salir"<<endl
                   <<"1-Para conectarse al servidor"<<endl
                   <<"================================================="<<endl;
            std::cin>>i;
            if (i==0){
                std::cout<<"Cliente desconectado"<<endl;
                exit(-1);
            }if (i==1){
                std::cout<<"Ingrese el puerto del servidor"<<endl;
                std::cin>>port;
                XmlRpc::XmlRpcClient c("localhost", port); 
                while (i!=0){
                    std::cout<<"             Control RPC del robot"<<endl
                            <<"================================================="<<endl
                            <<"Ingrese la accion a realizar:"<<endl
                            <<"0-Para desconectarse del servidor"<<endl
                            <<"1-Para apagar al robot"<<endl
                            <<"2-Para encender el robot"<<endl
                            <<"================================================="<<endl;
                    std::cin>>i;
                    if (i==0){
                        std::cout<<"Desconectado"<<endl;
                        exit(-1);
                    }if (i==1){
                        c.execute("apagar",sinArgs,resultado);
                        std::cout << resultado << "\n";
                    }if (i==2){
                        c.execute("encender",sinArgs,resultado);
                        std::cout << resultado << "\n";
                        while (i!=100){
                            std::cout<<"             Control RPC del robot"<<endl
                            <<"================================================="<<endl
                            <<"Ingrese el modo de operacion del robot:"<<endl
                            <<"0-Modo manual"<<endl
                            <<"1-Modo automatico"<<endl
                            <<"2-Apagar"<<endl
                            <<"3-Desconectarse"<<endl
                            <<"================================================="<<endl;
                            std::cin>>i;
                            if (i==0){
                                unArg=i;
                                c.execute("modo",unArg,resultado);
                                std::cout<<resultado<<"\n";
                                std::cout<<"             Control RPC del robot"<<endl
                                <<"================================================="<<endl
                                <<"Ingrese la accion a realizar::"<<endl
                                <<"0-Para desconectarse del servidor"<<endl
                                <<"1-Para apagar al robot"<<endl
                                <<"2-Posicionar extremo"<<endl
                                <<"3-Cambiar estado del efector"<<endl
                                <<"4-Homing"<<endl
                                <<"5-Reporte"<<endl
                                <<"6-Borrar archivo"<<endl
                                <<"7-Setear velocidad de funcionamiento"<<endl
                                <<"================================================="<<endl;
                                std::cin>>i;
                                if (i==0){
                                    std::cout<<"Desconectado"<<endl;
                                    exit(-1);
                                }if (i==1){
                                    c.execute("apagar",sinArgs,resultado);
                                    std::cout << resultado << "\n\n";
                                    i=100;
                                }if (i==2){
                                    char args[20];
                                        std::cout<<"Ingrese los angulos de rotacion de cada articulacion de la siguiente manera:\n A,B,C"<<endl;
                                        std::cin.ignore();
                                        std::cin.getline(args,20);
                                        Args=args;
                                        c.execute("set_posicion",Args,resultado);
                                        std::cout << resultado << "\n";
                                    
                                }if (i==3){
                                    int e;
                                    std::cout<<"Ingrese 0 para abrir la pinza o 1 para cerrarla"<<endl;
                                    std::cin>>e;
                                    unArg=e;
                                    c.execute("set_pinza",unArg,resultado);
                                    std::cout << resultado << "\n\n";
                                }if (i==4){
                                    c.execute("homing",sinArgs,resultado);
                                    std::cout << resultado << "\n\n";
                                }if (i==5){
                                    c.execute("get_info",sinArgs,resultado);
                                    std::cout << resultado << "\n";
                                }if(i==6){
                                    c.execute("borrar_archivo",sinArgs,resultado);
                                    std::cout << resultado << "\n\n";
                                }if(i==7){
                                    std::cout<<"\nIntroduzca la velocidad de las articulaciones en [rad/s]"<<endl;
                                    std::cin>>vel;
                                    unArg=vel;
                                    c.execute("velocidad",unArg,resultado);
                                    std::cout << resultado << "\n\n";
                                }
                            }else if (i==1){
                                int flag=1;
                                unArg=i;
                                c.execute("modo",unArg,resultado);
                                std::cout<<resultado<<"\n";
                                std::cout<<"\n=============================================\nIniciando posicionamiento automatico"<<endl;
                                while (flag!=0){
                                    if (resultado=="Fin"){
                                        std::cout <<"Ejecucion automatica finalizada\n=============================================\n"<<endl;
                                        flag=0;
                                    }else{
                                        c.execute("set_posicion",unArg,resultado);
                                        std::cout << resultado << "\n";
                                    }
                                }
                            }else if (i==2){
                                c.execute("apagar",sinArgs,resultado);
                                std::cout << resultado << "\n\n";
                                i=100;
                            }else if (i==3){
                                std::cout<<"Desconectado"<<endl;
                                exit(-1);
                            }
                        }
                    }
                }       
            }
        }

    }catch(XmlRpc::XmlRpcException e){
        cout << "Error numero " << e.getCode() << ", " << e.getMessage() << endl; 
    }
    return 0;
}