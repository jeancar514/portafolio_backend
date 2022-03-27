from flask import Flask, request,jsonify
import pywhatkit
import datetime
import sendgrid
from sendgrid.helpers.mail import *
from flask_cors import CORS, cross_origin


app = Flask('__name__')
CORS(app)

@cross_origin()
@app.route('/', methods=['POST'])
def leo():
    
    envio = request.json['envio']
    if(envio == "correo"):
        # email
        nombre = request.json['nombre']
        correo = request.json['correoelectronico']
        mensaje = request.json['mensaje']
        miCorreo = 'jeancarleonardo514@gmail.com'
        print(nombre)

        sg = sendgrid.SendGridAPIClient(api_key='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')

                
        de_correo = Email(correo)
        para_correo= To(miCorreo,substitutions={
            '-nombre-':nombre,
            '-correo-':correo,
            '-mensaje-':mensaje,
        })

        html_content =  """
            <p>Estamos revisando tu portafolio<p>
            <p>Nombre : -nombre- <p>
            <p>Correo : -correo- <p>
            <p>Mensaje : -mensaje- <p>
            """

        mail = Mail(miCorreo,para_correo,'Estamos observando tu portafolio',html_content=html_content)
        response = sg.client.mail.send.post(request_body=mail.get())

    if(envio == "whatsapp"):
        # mensaje whatsapp
        fechaActual= datetime.datetime.now()

        hora = int(datetime.datetime.strftime(fechaActual,'%H'))
        min =  1 + int(datetime.datetime.strftime(fechaActual,'%M'))
        print(hora,min)

        # Send a WhatsApp Message to a Contact 
        pywhatkit.sendwhatmsg("+584124696380", "Hola jeancar estamos observando tu portafolio",hora,min)
    return jsonify({'listo':"listo"})


if (__name__ =='__main__'):
    app.run(debug=True)

        # if(envio == "whatsapp" ):    
        #     enviarWhatsapp(envio)
        # elif(envio == "correo" ):
        #     enviarCorreo(envio)


    #     def enviarCorreo(nombre,correo,mensaje):
    #             miCorreo = 'jeancarleonardo514@gmail.com'
    #             print(nombre)

    #             sg = sendgrid.SendGridAPIClient(api_key='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')
    #             print(nombre)
                
    #             de_correo = Email(correo)
    #             para_correo= To(miCorreo,substitutions={
    #                 '-nombre-':nombre,
    #                 '-correo-':correo,
    #                 '-mensaje-':mensaje,
    #             })
    #             print(nombre)


    #             html_content =  """
    #                 <p>Estamos revisando tu portafolio<p>
    #                 <p>Nombre : -nombre- <p>
    #                 <p>Correo : -correo- <p>
    #                 <p>Mensaje : -mensaje- <p>
    #             """
    #             print(nombre)
    #             mail = Mail(miCorreo,para_correo,'Observando tu portafolio',html_content=html_content)
    #             response = sg.client.mail.send.post(request_body=mail.get())

    #     def enviarWhatsapp():
    #         # mensaje whatsapp
    #         fechaActual= datetime.datetime.now()

    #         hora = int(datetime.datetime.strftime(fechaActual,'%H'))
    #         min =  1 + int(datetime.datetime.strftime(fechaActual,'%M'))
    #         print(hora,min)

    #         # Send a WhatsApp Message to a Contact 
    #         pywhatkit.sendwhatmsg("+584124696380", "Hola jeancar desde tu portafolio",hora,min)

    #     if(envio == "whatsapp" ):    
    #         enviarWhatsapp(envio)
    #     elif(envio == "correo" ):
    #         enviarCorreo(envio)

    #     return jsonify({'listo':"listo"})
    # except:
    #     return jsonify({'fallo':"fallo"})
    

    