import streamlit as st
import requests
import time
import json

st.set_page_config(
     page_title="Language - Translator",
     page_icon="random",
     layout="centered",
     menu_items={
        'Get help': "https://google.com/",
        'About': "Made With Love And Lots Of Efforts!!"
     }
 )

st.title("The Ultimate Translator")


#Translator

input_language = st.selectbox("Input Text Language:", ["Auto-Detect","en-English", "fr-French","hi-Hindi",
"ps-Pashto", "pt-Portuguese","af-Afrikaans ",   "sq-Albanian ",   "am-Amharic ",   "ar-Arabic ",   "hy-Armenian ",   
"as-Assamese ",   "az-Azerbaijani ",   "bn-Bangla ",   "ba-Bashkir ",   "bs-Bosnian ",   "bg-Bulgarian ",   
"yue-Cantonese (Traditional) ",   "ca-Catalan ",   "lzh-Chinese (Literary) ",   "zh-Hans-Chinese Simplified ",
"zh-Hant-Chinese Traditional ",   "hr-Croatian ",   "cs-Czech ",   "da-Danish ",   "prs-Dari ",   "dv-Divehi ",  
 "nl-Dutch ",   "en-English ",   "et-Estonian ",   "fj-Fijian ",   "fil-Filipino ",   "fi-Finnish ",   "fr-French ",   
"fr-CA-French (Canada) ",   "ka-Georgian ",   "de-German ",   "el-Greek ",   "gu-Gujarati ",   "ht-Haitian Creol ", 
"he-Hebrew ",   "hi-Hindi ",   "mww-Hmong Daw ",   "hu-Hungarian ",   "is-Icelandic ",   "id-Indonesian ",   "iu-Inuktitut ",
"ga-Irish ",   "it-Italian ",   "ja-Japanese ",   "kn-Kannada ",   "kk-Kazakh ",   "km-Khmer ",   
"tlh-Latn-Klingon (Latin) ",   "ko-Korean ",   "ku-Kurdish (Central) ",   "kmr-Kurdish (Northern) ",   
"ky-Kyrgyz ",   "lo-Lao ",   "lv-Latvian ",   "lt-Lithuanian ",   "mk-Macedonian ",   "mg-Malagasy ",   
"ms-Malay ",   "ml-Malayalam ",   "mt-Maltese ","mi-Māori",
"mr-Marathi","mn-Cyrl-Mongolian (Cyrillic)","mn-Mong-Mongolian (Traditional)","my-Myanmar (Burmese)",
"ne-Nepali","nb-Norwegian","or-Odia","ps-Pashto","fa-Persian","pl-Polish","pt-Portuguese (Brazil)","pt-PT-Portuguese (Portugal)",
"pa-Punjabi","otq-Querétaro Otomi","ro-Romanian","ru-Russian","sm-Samoan","sr-Cyrl-Serbian (Cyrillic)",
"sr-Latn-Serbian (Latin)","sk-Slovak","sl-Slovenian",
"es-Spanish","sw-Swahili","sv-Swedish","ty-Tahitian",
"ta-Tamil","tt-Tatar","te-Telugu","th-Thai",
"bo-Tibetan","ti-Tigrinya","to-Tongan","tr-Turkish","tk-Turkmen","uk-Ukrainian","ur-Urdu","ug-Uyghur",
"uz-Uzbek (Latin)","vi-Vietnamese","cy-Welsh","yua-Yucatec Maya"]).split("-")[0]


output_language = st.selectbox("Translation Language:", ["en-English", "fr-French", "es-Espanoles",
"hi-Hindi","ps-Pashto", "pt-Portuguese","af-Afrikaans ",   "sq-Albanian ",   "am-Amharic ",   "ar-Arabic ",   "hy-Armenian ",   
"as-Assamese ",   "az-Azerbaijani ",   "bn-Bangla ",   "ba-Bashkir ",   "bs-Bosnian ",   "bg-Bulgarian ",   
"yue-Cantonese (Traditional) ",   "ca-Catalan ",   "lzh-Chinese (Literary) ",   "zh-Hans-Chinese Simplified ",
"zh-Hant-Chinese Traditional ",   "hr-Croatian ",   "cs-Czech ",   "da-Danish ",   "prs-Dari ",   "dv-Divehi ",  
 "nl-Dutch ",   "en-English ",   "et-Estonian ",   "fj-Fijian ",   "fil-Filipino ",   "fi-Finnish ",   "fr-French ",   
"fr-CA-French (Canada) ",   "ka-Georgian ",   "de-German ",   "el-Greek ",   "gu-Gujarati ",   "ht-Haitian Creol ", 
"he-Hebrew ",   "hi-Hindi ",   "mww-Hmong Daw ",   "hu-Hungarian ",   "is-Icelandic ",   "id-Indonesian ",   "iu-Inuktitut ",
"ga-Irish ",   "it-Italian ",   "ja-Japanese ",   "kn-Kannada ",   "kk-Kazakh ",   "km-Khmer ",   
"tlh-Latn-Klingon (Latin) ",   "ko-Korean ",   "ku-Kurdish (Central) ",   "kmr-Kurdish (Northern) ",   
"ky-Kyrgyz ",   "lo-Lao ",   "lv-Latvian ",   "lt-Lithuanian ",   "mk-Macedonian ",   "mg-Malagasy ",   
"ms-Malay ",   "ml-Malayalam ",   "mt-Maltese ","mi-Māori",
"mr-Marathi","mn-Cyrl-Mongolian (Cyrillic)","mn-Mong-Mongolian (Traditional)","my-Myanmar (Burmese)",
"ne-Nepali","nb-Norwegian","or-Odia","ps-Pashto","fa-Persian","pl-Polish","pt-Portuguese (Brazil)","pt-PT-Portuguese (Portugal)",
"pa-Punjabi","otq-Querétaro Otomi","ro-Romanian","ru-Russian","sm-Samoan","sr-Cyrl-Serbian (Cyrillic)",
"sr-Latn-Serbian (Latin)","sk-Slovak","sl-Slovenian",
"es-Spanish","sw-Swahili","sv-Swedish","ty-Tahitian",
"ta-Tamil","tt-Tatar","te-Telugu","th-Thai",
"bo-Tibetan","ti-Tigrinya","to-Tongan","tr-Turkish","tk-Turkmen","uk-Ukrainian","ur-Urdu","ug-Uyghur",
"uz-Uzbek (Latin)","vi-Vietnamese","cy-Welsh","yua-Yucatec Maya"]).split("-")[0]

text_to_translate = st.text_area("Enter The Text To Be Translated: ")

url = "https://cheap-translate.p.rapidapi.com/translate"

payload = "{\"fromLang\" : \"auto-detect\", \"text\": \"%s\", \"to\": \"%s\"}"%(text_to_translate, output_language)

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "1bb4ae38e4msh41488d47c23c2bep1ceec9jsncf9727ecbf11",
	"X-RapidAPI-Host": "cheap-translate.p.rapidapi.com"
}


translate_button = st.button("TRANSLATE")

if translate_button:
    if text_to_translate == "":
        st.markdown("***You Haven't Entered Any Text to be Translated***")
    else:
        with st.spinner('Translating Your Text .....'):
            time.sleep(2.5)
        st.success('Translated Text: ')
        if input_language == output_language:
            st.markdown(text_to_translate)
        else:
            try:
                response = requests.request("POST", url, data=payload, headers=headers)
                output_text = json.loads(response.text)
                st.markdown(output_text['translatedText']) 
            except:
                st.markdown("***!!! An Error Has Occured !!!***")
