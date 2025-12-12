import os
from dotenv import load_dotenv


load_dotenv()

AVITO_URL="https://www.avito.ru/irkutsk/telefony/mobilnye_telefony/apple-ASgBAgICAkS0wA3OqzmwwQ2I_Dc?cd=1&context=H4sIAAAAAAAA_0SQzXLaMACE34VrD5UNboozPRA5VuWRzdiALHFDUvBPZEPjfzp9944MaY9arbT77cm13N-NawF3IS8fH2-yLS714rlxHcd2F7huJa78UiHdCz0UWz0UsqKDQH55pENB_KE4stycO86Sq7AdicurxC3cAd7HjUIbQLy4V4jgCL0CUsbdGoWAkySLECHQSzIFvwDylGQtnABhSdaiF8BJ3LTIA_wpKRRcAXLIADnHTQS_Au7F_ewJs-FXe5Uo70XFYDc5EhejxPVLw9NIi5R2yr935hVtxFLd76tES1vXQh-1rKP_nSunl5WVC2jlAtHJvDV8AunutIyMR7xZM_-oUnqb_zb71L51ZIHDIP7GYPDoQx9ZUa4QrcUycHaHROLysoqg0cee2z44pevuodthmTnRbdMwGAycBblgc-YTg3gM9xs73CvjG7eenEJPjuE0Sly-jqHHx63pUsb2di9v0e6fvgrvurX1DkP401obHoXo6nMXEMy7fweExb3ZmZOk_OROKTih9fuD63ZM_Ynb-VlW9P3EAs2XicS1pc47_GPx_OdvAAAA___oRMj_SQIAAA&s=104"

BOT_TOKEN=os.getenv('BOT_TOKEN')
CHROME_DRIVER_PATH=os.getenv('CHROME_DRIVER_PATH')


DEBUG_LOG_PATH=os.getenv('DEBUG_LOG_PATH')

tg_ids = {
    1:os.getenv('TG_ID'),
    2:os.getenv('TG_ID2')
}
sellers_black_list = (os.getenv('BL_ID1'),
                      os.getenv('BL_ID2'),
                      os.getenv('BL_ID3'),
                      os.getenv('BL_ID4'),
                      os.getenv('BL_ID5'),
                      os.getenv('BL_ID6'),
                      os.getenv('BL_ID7'),
                      os.getenv('BL_ID8'),
                      os.getenv('BL_ID9'),
                      )

TTL_SECONDS = 2*24*60*60  # TTL = 2 дня