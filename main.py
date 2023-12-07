from fastapi import FastAPI
from database.db import Base, engine
from routers import user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mi Proyecto de SWII",description="Este es mi primer proyecto en fastapi para el profe reinel",
              version="10.2.4")

app.include_router(user.router, tags=["User"])

@app.get("/", tags=["Main"])
def main():
    """
    predict

    Performs the features extracting from the format given:

    Args:
        background_tasks:
        encripted:
        message(dict): A dictionary containing scraped text. The must keys are:

            - "link" (str): scraped vacancy link without query params
            - "data" (str): full text of the description of the scraped vacancy

    Returns:
        dict: A dictionary containing all the feature of a vacancy. The must keys are:

            - "vacancy_name" (varchar(150)): This is a field that represents the name or title of a job opening or vacancy that a company is looking to fill. It is typically a string of characters with a maximum length of 150 characters.
            - "description" (text): This field contains a detailed description of the job opening or vacancy, including the responsibilities, qualifications, and other important information about the position. It can contain a large amount of text and is often used to attract potential candidates.
            - "company" (varchar(150)): This field represents the name of the company that is offering the job opening or vacancy. It is typically a string of characters with a maximum length of 150 characters.
            - "location" (varchar(150)): This field represents the physical location where the job opening or vacancy is based. It can be a city, state, country, or even a specific address. It is typically a string of characters with a maximum length of 150 characters.
            - "work_modality" (text): This field represents the type of work modality that the job opening or vacancy is offering. It can be full-time, part-time, remote, or any other type of work arrangement. It is typically a string of characters that can contain a few words.
            - "seniority_level" (text): This field represents the seniority level of the position being offered. It can be entry-level, mid-level, senior-level, or any other level that the company uses to classify its positions. It is typically a string of characters that can contain a few words.
            - "office_modality" (text): This field represents the type of office modality that the job opening or vacancy is offering. It can be on-site, hybrid, or any other type of office arrangement. It is typically a string of characters that can contain a few words.
            - "wage_min" (numeric(9)): This field represents the minimum wage or salary that the job opening or vacancy is offering. It is typically a numeric value with a maximum length of 9 digits.
            - "wage_max" (numeric(9)): This field represents the maximum wage or salary that the job opening or vacancy is offering. It is typically a numeric value with a maximum length of 9 digits.
            - "years_experience_max" (numeric(3)): This field represents the maximum number of years of experience that the company is looking for in a candidate for the job opening or vacancy. It is typically a numeric value with a maximum length of 3 digits.
            - "years_experience_min" (numeric(3)): This field represents the minimum number of years of experience that the company is looking for in a candidate for the job opening or vacancy. It is typically a numeric value with a maximum length of 3 digits.
            - "languages" (dict): This field represents the languages that the company is looking for in a candidate for the job opening or vacancy, along with the level of proficiency required for each language. It is typically a dictionary that contains two keys:
                - "language" (string): key is a string that represents the name of the language.
                - "level_id" (string): key is a string that represents the level of proficiency required for that language.
            - "skills_custom" (character varying[]): This field represents any additional custom skills that the company is looking for in a candidate for the job opening or vacancy. It is a character varying array, which means it is a field that can store multiple values of strings. The values in this field are typically skills that are specific to the job or the company, and may not be included in a standard list of required skills for the position.

    Example_demo:

            {
                "link":"https://co.indeed.com/viewjob?jk=6eedfc9f2e7cda65&l=Bogota&from=web&advn=1750309468638320&adid=411819914&ad=-6NYlbfkN0DeICuqtN8bFRbso-JB9O9XtIJkeka4pe_fnQS52bBlzvAJyzk67AxrKTUo-w4zJ2NcM6IahZgVtNNNd2PoNtRXjWTOoxOh0XiGEKtpY_sPBc4Sm0_BtkYZtzzeL5_Oal50c_PS6nC32Kl2UJSZdopk7Azd843YH88o1EBV-zsPLt4ObNgxDegrxYdnZimWtfbEd177hNupvXEcC4oRx1zp0Y8uv0lmUpzrtYXyQPKPtLyo2i-y-B9WMtWMrbsrhES3gYZBaZNUpvLyQPKYAxdOB1gVvYgNhKsENUtQf9X5C5Z-BT7UXF1kD5nAva_kgnmBEI-BKnbwD9O0TlT8IjcLO3GWUGMC0MyVvDyNCDc-bwMZdVqqeX7lWih4dPX0MjuGvP_yuX1DPREqpPIiiI3e1C9fOHFRwBrvZIt63XDnfw%3D%3D&pub=4a1b367933fd867b19b072952f68dceb&xkcb=SoCF-_M3PkrnrbWZQZ0JbzkdCdPP&vjs=3",
                "data": "IrdirectamentealcontenidoprincipalBuscarempleosEvaluacionesdeempresaBuscarsalariosSubirtuHVIngresarEmpresas/PublicarempleosIniciodelcontenidoprincipalQuéDóndeBuscarempleosNeuralNetworkScientistTemporaryWolframBogotá,Cundinamarca$4.663.430-$6.528.802pormes-Tiempocompleto,Mediotiempo,PrácticascreaunacuentadeIndeedantesdecontinuaralapáginawebdelaempresa.ContinuarparapostularDetallesdelempleoNohaycoincidenciassegúnlaspreferenciasdeempleoSalario$4.663.430-$6.528.802pormesTipodeempleoTiempocompletoMediotiempoPrácticasDescripcióncompletadelempleoWolfram,creatorofMathematica,Wolfram|AlphaandWolframLanguage,isseekingaself-motivatedandproactiveNeuralNetworkScientisttojoinitsAlgorithmsR&Dteam.TheNeuralNetworkScientistwillworkwiththeSound&Visionteamtohelpwithmassiveopenonlinecourse(MOOC)contentcreation.Thisisatemporaryposition.ResponsibilitiesWorkingwithdevelopersandresearcherstowritethebulkofthecontentfortheneuralnetworkMOOCbasedonexistingcontentCreatingnewcontentandexamplestoshowusesandapplicationsoftheneuralnetworksQualificationsMaster’sorPhDincomputerscience,engineering,math,physicsorarelatedtechnicalorquantitativefieldExcellentfamiliaritywithdeepneuralnetworksExcellentwrittenskillsAbilitytoworkindependentlyandaspartofateamFluentinEnglishPreferredqualificationsExperiencewithspecificapplicationdomainsofneuralnetworks(computervision,NLP,speechrecognition,etc.)Hands-onexperiencewithWolframLanguageExcellentoralpresentationskillsLocation:RemoteWolframisanequalopportunityemployerandvaluesdiversityatitscompany.Women,peopleofcolor,membersoftheLGBTQcommunity,individualswithdisabilitiesandveteransarestronglyencouragedtoapply.JobTypes:Full-time,Part-time,InternshipContractlength:3monthsPart-timehours:20-40perweekPay:$4,663,430-$6,528,802permonthHiringInsightsSeestácontratando1candidatoparaestepuestoActividaddelempleoLaempresaevaluóelempleohace20díasPublicadohace19díasReportarempleoEmpleosdeScientistenBogotá,CundinamarcaEmpleosdeWolframenBogotá,CundinamarcaScientistsalariosenBogotá,CundinamarcaSeguirRecibetodoslosnuevosempleosdeWolframWolframFoundedbyStephenWolframin1987,WolframResearchisoneoftheworld'smostrespectedcomputer,web,andcloudsoftwarecompanies—as...VerempleosSalariosPaísesAcercadeCentrodeasistencia©2023IndeedAccesibilidadenIndeedCentrodeprivacidadCookiesPrivacidadCondicionesDejaquelasempresasteencuentrenPublicatuCV"
            }
    """

    return {"message": "Hello World"}