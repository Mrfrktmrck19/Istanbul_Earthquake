import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


def main():

    # PNG resmini yükle
    image = Image.open("1preview2.png")
    # Resmi göster
    st.image(image, use_column_width=True)



    st.write("<span style='color:black; font-weight: bold;'>Türkiye, jeolojik yapısı gereği dünya üzerinde depremlerin sıkça yaşandığı bölgelerden birinde bulunmaktadır. Özellikle Türkiye'nin kuzeyinde yer alan Kuzey Anadolu Fay Hattı, ülkemizi deprem riski yüksek bir bölge haline getirmektedir. Bu gerçekle karşı karşıya olan bir toplum olarak, deprem riskini anlamak, depremleri önceden tahmin etmek ve bu doğal felaketlerin olası etkilerine karşı hazırlıklı olmak büyük bir önem taşımaktadır.</span>",
             unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>Bu proje, Türkiye'nin deprem riski altındaki bölgelerindeki deprem faaliyetlerini incelemek ve gelecekteki olası depremleri tahmin etmek amacıyla gerçekleştirilmiştir. Aynı zamanda, projemiz İstanbul'da olası bir depremin etkilerini analiz etmeye odaklanmış ve bu büyük metropoldeki riskleri anlamamıza yardımcı olacak veriler sunmayı hedeflemektedir</span>",
        unsafe_allow_html=True)

    # https://cdn.pixabay.com/photo/2017/02/26/04/47/cracks-2099531_1280.jpg
    page_by_img = """
        <style>
        [data-testid="stAppViewContainer"]{
        background: url("https://cdn.create.vista.com/api/media/small/394838678/stock-photo-damaged-wall-gray-background-crack");
        background-size: cover;top: 0px}

        [data-testid="stHeader"]{
        background-color: rgba(0,0,0,0);
         }

        [data-testid="stToolbar"]{
        right: 2rem;}
        </style>
         """
    st.markdown(page_by_img, unsafe_allow_html=True)
    st.text("")
    st.text("")


    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Türkiye'de Gerçekleşmiş Depremler</h2>",
                unsafe_allow_html=True)

    st.write(
        "<span style='color:black; font-weight: bold;'>Türkiye'de önceden gerçekleşen depremleri Power BI kullanarak analiz ettik. Bu da geçmiş depremlerin dağılımını incelemeye yardımcı oldu. Bu analiz, Türkiye'nin deprem riskini daha iyi anlamamıza ve gelecekteki depremlere hazırlıklı olmamıza katkı sağlayacak önemli veriler sunmaktadır.</span>",
        unsafe_allow_html=True)

    # Power BI gömme kodunu gömme
    power_bi_embed_code = """
    <iframe title="FJBCGC" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=3cc53d43-eb3b-4b2e-b198-8d7b87befb4c&autoAuth=true&ctid=fda4d358-3750-4b5b-9588-c0294ccf291e" frameborder="0" allowFullScreen="true"></iframe>    """
    st.markdown(power_bi_embed_code, unsafe_allow_html=True)


    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Yıllara Göre Deprem Büyüklükleri</h2>",
                unsafe_allow_html=True)

    st.write(
        "<span style='color:black; font-weight: bold;'>Power BI kullanarak gerçekleştirdiğimiz analizler sonucunda üç önemli görsel oluşturduk. İlk görsel, yıllara göre deprem büyüklüklerini inceleyerek her yıl meydana gelen deprem sayısını ve bu depremlerin büyüklük ortalamasını gösteriyor. Bu sayede zaman içinde deprem aktivitesinin dağılımını izleyebiliyoruz.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>İkinci görsel, depremlerin ortalama derinliği ile ortalama büyüklüğünü karşılaştırarak deprem olaylarının hangi derinliklerde daha yaygın olduğunu ve büyüklüklerinin ne kadar değişken olduğunu gösteriyor. Bu analiz, depremlerin yer altındaki kaynaklarına dair önemli bilgiler sunuyor.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>Üçüncü görsel ise enlem, boylam ve oluş tarihine göre gruplandırılmış depremlerin büyüklük ortalamalarını gösteriyor. Bu görsel, depremlerin coğrafi dağılımını ve tarihsel eğilimlerini değerlendirmemize yardımcı oluyor.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'></span>",
        unsafe_allow_html=True)
    # Power BI gömme kodunu gömme
    power_bi_embed_code = """
    <iframe title="gümgümbür" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=68261b71-2066-422a-8b2f-25f79502a480&autoAuth=true&ctid=fda4d358-3750-4b5b-9588-c0294ccf291e" frameborder="0" allowFullScreen="true"></iframe> """
    st.markdown(power_bi_embed_code, unsafe_allow_html=True)



    # Başlık

    #st.markdown("<h2 style='color:#8a3a3a; font-weight: bold;'>İletişim Bilgileri</h2>",
    #            unsafe_allow_html=True)

    #st.markdown("<h2 style='color:#8a3a3a; font-weight: normal;'>E-posta</h2>",
    #            unsafe_allow_html=True)


    #st.write("rminekorkmaz@gmail.com")

    # İletişim formu eklemek için bir metin kutusu kullanabilirsiniz
    #st.header("İletişim Formu")
    #isim = st.text_input("İsim")
    #email = st.text_input("E-posta")
    #mesaj = st.text_area("Mesaj")
    #gonder = st.button("Gönder")

    # Gönder düğmesine tıklanırsa işlem yapabilirsiniz
    #if gonder:
     #   st.success("Mesajınız gönderildi!")


def hakkimizda():
    image = Image.open("biz.png")
    st.image(image, caption="PNG Resmi", use_column_width=True)




    page_by_img = """
        <style>
        [data-testid="stAppViewContainer"]{
        background: url("https://images.pexels.com/photos/7806186/pexels-photo-7806186.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
        background-size: cover;top: 0px}

        [data-testid="stHeader"]{
        background-color: rgba(0,0,0,0);
         }

        [data-testid="stToolbar"]{
        right: 2rem;}
        </style>
         """
    st.markdown(page_by_img, unsafe_allow_html=True)

# Deprem Nedir sayfası
def deprem_nedir():

    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Deprem Nedir?</h2>",unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>Deprem,yer yüzeyinde meydana gelen ani ve şiddetli sarsıntılardır. Bu sarsıntılar, yer altındaki büyük kayaların ani bir şekilde hareket etmesi sonucu oluşurlar. Depremler, yer kabuğundaki gerilimlerin aniden serbest bırakılmasıyla meydana gelirler.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>Dünya, devamlı olarak hareket halindedir. Yer kabuğu denilen dış tabaka, büyük kara parçalarının ve okyanusların altında yer alır. Bu kabuk, sürekli olarak yerin içindeki ısınma ve soğuma nedeniyle hareket eder. Ancak, bu hareket düzensizdir ve yer kabuğu parçaları birbirine sürtünürken veya birbirlerinden uzaklaşırken büyük gerilimler oluştururlar.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>Depremler, bu gerilimler serbest bırakıldığında meydana gelir. Aniden serbest bırakılan enerji, yer yüzeyinde titreşimlere yol açar. Bu titreşimler, binaları, yolları ve diğer yapıları sallayabilir veya zarar verebilir.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>Depremler sadece yer yüzeyinde sallanmakla kalmaz, aynı zamanda yer altında da oluşabilirler. Depremler genellikle birkaç saniye ile birkaç dakika arasında sürer, ancak etkileri uzun süre devam edebilir.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>Depremler doğal olaylardır ve dünya üzerinde sıkça meydana gelirler. Bu nedenle, depremlere karşı hazırlıklı olmak önemlidir. Binaların depreme dayanıklı olması, deprem sırasında güvende olmanın en önemli yollarından biridir.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>Unutmayın ki depremler doğal bir olgudur, ancak doğru önlemler alarak ve bilinçli bir şekilde davranarak bu doğal tehlikelere karşı korunabiliriz.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>Deprem Nedir? ile ilgili izlemenizi önerdiğimiz video:</span>",
        unsafe_allow_html=True)
    youtube_url = "https://www.youtube.com/watch?v=yMMnhRdzIqM"
    st.video(youtube_url)

    page_by_img = """
            <style>
            [data-testid="stAppViewContainer"]{
            background: url("https://cdn.create.vista.com/api/media/small/394838678/stock-photo-damaged-wall-gray-background-crack");
            background-size: cover;top: 0px}

            [data-testid="stHeader"]{
            background-color: rgba(0,0,0,0);
             }

            [data-testid="stToolbar"]{
            right: 2rem;}
            </style>
             """
    st.markdown(page_by_img, unsafe_allow_html=True)
    st.text("")
    st.text("")

# Deprem Çeşitleri sayfası
def deprem_cesitleri():
    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Deprem Çeşitleri</h2>",unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>1.Tektonik Depremler: Bu tür depremler, yer kabuğundaki büyük kara parçalarının veya levhaların birbirine sürtünmesi veya çarpışması sonucu meydana gelir. Tektonik depremler dünyanın her yerinde görülebilir ve genellikle en büyük ve en yıkıcı depremlerdir.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>2.Volkanik Depremler: Volkanik depremler, volkanların patlaması veya lavın yer altında hareketi nedeniyle ortaya çıkar. Volkanlarla yakından ilişkilidirler ve patlama sırasında ortaya çıkan enerjinin bir sonucu olarak oluşurlar.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>3.Yer İçi Depremler: Bu tür depremler, yerin derinliklerinde meydana gelir. Yer kabuğunun altındaki çatlaklarda veya fay hatlarında gerçekleşirler. Genellikle yer yüzeyine yakın olmadıkları için daha az zarar verirler.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>4.Yer Üstü Depremler: Yer üstü depremler, yer yüzeyinin hemen altında meydana gelir. Bu tür depremler, genellikle yapıların zarar görmesine neden olurlar ve insanlar için daha fazla tehlike oluştururlar.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>5.Denizaltı Depremler: Deniz tabanının altında gerçekleşen bu depremler, deniz suyunu sallayarak tsunamilere neden olabilirler. Büyük denizaltı depremleri, kıyı bölgelerinde büyük zararlara yol açabilir.</span>",
        unsafe_allow_html=True)
    st.text("")
    st.write(
        "<span style='color:black; font-weight: bold;'>Her tür deprem, farklı nedenlerle meydana gelir ve farklı etkilere sahiptir. Ancak hepsi, yer kabuğundaki gerilimlerin serbest bırakılması sonucu ortaya çıkarlar. Depremlere karşı dikkatli olmak ve deprem hazırlığı yapmak, yaşadığınız bölgeye bağlı olarak hayati öneme sahiptir.</span>",
        unsafe_allow_html=True)
    page_by_img = """
                <style>
                [data-testid="stAppViewContainer"]{
                background: url("https://cdn.create.vista.com/api/media/small/394838678/stock-photo-damaged-wall-gray-background-crack");
                background-size: cover;top: 0px}

                [data-testid="stHeader"]{
                background-color: rgba(0,0,0,0);
                 }

                [data-testid="stToolbar"]{
                right: 2rem;}
                </style>
                 """
    st.markdown(page_by_img, unsafe_allow_html=True)
    st.text("")
    st.text("")


# Deprem Ölçümü sayfası
def deprem_olcumu():
    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Deprem Ölçümü</h2>",unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>Deprem ölçümü, yer yüzeyindeki deprem etkilerini kaydeden ve ölçen bir bilim dalıdır. Bu ölçümler, depremlerin şiddetini, derinliğini ve yerini belirlememize yardımcı olur</span>",
        unsafe_allow_html=True)
    st.text("")
    st.write(
        "<span style='color:black; font-weight: bold;'>1.Sismometreler (Sismograf): Deprem ölçümünün en temel aracıdır. Sismometreler, yer yüzeyindeki sarsıntıları algılayan hassas cihazlardır. "
        "Bir sismometre, zeminin sarsılmasına karşı duyarlı bir kütle içerir ve bu kütle yer hareketiyle birlikte kayar. "
        "Bu kayma, bir grafik kaydedici üzerine işlenir ve depremin şiddeti ve süresi hakkında bilgi sağlar.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>2.Deprem Dalgaları: Sismometreler, yer yüzeyindeki deprem dalgalarını kaydeder. Bu dalgalar, P-dalgaları, S-dalgaları ve yüzey dalgaları olmak üzere farklı türlerde gelir. "
        "P-dalgaları en hızlı yayılan ve ilk sarsıntıyı temsil eder. "
        "S-dalgaları ise daha yavaş yayılır ve daha büyük zararlara yol açabilir.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>3.Deprem Büyüklüğü ve Derinliği: Sismometreler sayesinde, bir depremin büyüklüğü ve derinliği ölçülebilir. "
        "Deprem büyüklüğü, genellikle Richter ölçeği veya Moment Magnitude ölçeği kullanılarak ifade edilir. "
        "Derinlik, depremin yerin yüzeyine ne kadar yakın veya uzak olduğunu gösterir.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>4.Deprem Haritası: Depremler dünya genelinde meydana geldiğinden, deprem haritaları oluşturmak önemlidir."
        "Bu haritalar, deprem riskini ve belli bölgelerin daha sık sarsıntılarla karşılaşma olasılığını gösterir. </span>",
        unsafe_allow_html=True)
    st.text("")
    st.write(
        "<span style='color:black; font-weight: bold;'>Deprem ölçümü, depremlerin neden olduğu zararı tahmin etmek ve deprem riski altındaki bölgelerde insanları korumak için kritik bir rol oynar. "
        "Bu ölçümler, bilim insanlarına, mühendislere ve acil durum yöneticilerine depremlere hazırlıklı olmak ve zararları en aza indirmek için önemli veriler sunar.</span>",
        unsafe_allow_html=True)


    page_by_img = """
               <style>
               [data-testid="stAppViewContainer"]{
               background: url("https://cdn.create.vista.com/api/media/small/394838678/stock-photo-damaged-wall-gray-background-crack");
               background-size: cover;top: 0px}

               [data-testid="stHeader"]{
               background-color: rgba(0,0,0,0);
                }

               [data-testid="stToolbar"]{
               right: 2rem;}
               </style>
                """
    st.markdown(page_by_img, unsafe_allow_html=True)
    st.text("")

# Deprem Güvenliği sayfası
def deprem_guvenligi():
    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Deprem Güvenliği</h2>",unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>Deprem güvenliği, depremlere karşı bireyleri ve toplulukları korumak için alınan önlemleri ve tedbirleri içeren bir konsepttir. "
        "Depremler doğal afetlerdir ve hazırlıksız yakalandıklarında büyük zararlara yol açabilirler. Bu nedenle, deprem güvenliği hayati bir öneme sahiptir.</span>",
        unsafe_allow_html=True)
    st.text("")
    st.write(
        "<span style='color:black; font-weight: bold;'>1.Deprem Anında Neler Yapılmalıdır? "
        "Deprem sırasında korunma önemlidir. Eğer kapalı bir mekândaysanız, masanızın altına veya bir iç duvarın yanına sığının. Eğer açık alandaysanız, düşme tehlikesi oluşturabilecek şeylerden uzak durun. Asansörleri kullanmaktan kaçının.</span>",
        unsafe_allow_html=True)
    youtube_url = "https://www.youtube.com/watch?v=oZeI0X40EEY"
    st.video(youtube_url)
    st.write(
        "<span style='color:black; font-weight: bold;'>2.Ev ve Bina Güvenliği:  Evlerin ve binaların depreme dayanıklı olması önemlidir. Yapılar, yerel bina kodlarına uygun olarak inşa edilmelidir. "
        "Ayrıca, kitaplık, ayna gibi düşebilecek nesneleri yatağınızın üzerine yerleştirmek ve su, gaz gibi tesisatları kontrol ettirmek de önemlidir.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:black; font-weight: bold;'>3.Acil Durum Hazırlıkları: Depremlere karşı hazırlıklı olmak, hayat kurtarabilir. "
        "Acil durum çantası hazırlamak, ailenizle birlikte toplanma noktalarını belirlemek ve iletişim planı oluşturmak, deprem anında organizasyonu kolaylaştırır.</span>",
        unsafe_allow_html=True)

    st.write(
        "<span style='color:black; font-weight: bold;'>4.Eğitim ve Bilinç: Deprem güvenliği ile ilgili bilinçli olmak çok önemlidir. Depremler hakkında bilgi edinmek, güvende olmanın ilk adımıdır. "
        "Ayrıca, deprem tatbikatları yaparak aileniz ve iş arkadaşlarınızla pratik yapmak da önemlidir.</span>",
        unsafe_allow_html=True)

    st.text("")
    st.write(
        "<span style='color:black; font-weight: bold;'>Deprem güvenliği, depremler gibi doğal afetlerin etkilerini minimize etmek için herkesin üzerine düşen sorumluluğu yerine getirmesi gereken bir konsepttir. "
        "Bu önlemler, can kayıplarını azaltabilir ve maddi zararları en aza indirebilir.</span>",
        unsafe_allow_html=True)

    page_by_img = """
                   <style>
                   [data-testid="stAppViewContainer"]{
                   background: url("https://cdn.create.vista.com/api/media/small/394838678/stock-photo-damaged-wall-gray-background-crack");
                   background-size: cover;top: 0px}

                   [data-testid="stHeader"]{
                   background-color: rgba(0,0,0,0);
                    }

                   [data-testid="stToolbar"]{
                   right: 2rem;}
                   </style>
                    """
    st.markdown(page_by_img, unsafe_allow_html=True)
    st.text("")


def istanbul_özel():
    st.title("İSTANBUL")
    st.write(
        "<span style='color:white; font-weight: bold;'>İstanbul Büyükşehir Belediyesi'nden elde edilen verilerle, hangi ilçelerin daha fazla risk altında olduğu, olası can kaybı, yaralanmalar, doğalgaz ve içme suyu borularının hasar durumu gibi kritik bilgilere odaklandık. Bu veriler, İstanbul'daki acil durum hazırlıklarının ve risk yönetiminin geliştirilmesine katkı sağlamayı amaçlamaktadır.</span>",
        unsafe_allow_html=True)

    st.text("")


    st.markdown("<h2 style='color:white; font-weight: bold;font-size:35px;'>İstanbul Can Kaybı ve Risk Görselleştirme</h2>",
                unsafe_allow_html=True)
    st.write(
        "<span style='color:white; font-weight: bold;'>1.Sayfada ilk olarak, İstanbul genelindeki toplam can kaybını ilçelere göre bir grafik üzerinde gösterdik. Bu görsel, hangi bölgelerin daha yüksek can kaybı riski taşıdığını hızlıca görmemize yardımcı oluyor.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:white; font-weight: bold;'>Ardından, her ilçede toplam can kaybı sayısını, toplam ağır yaralı sayısını, toplam hafif yaralı sayısını, toplam hastanede tedavi gören kişi sayısını, toplam doğalgaz borusu hasarını ve toplam içme suyu boru hasarı değerlerini özetleyen bir tablo oluşturduk. Bu tablo, her ilçedeki risklerin sayısal değerlerini sunarak detaylı bir bilgi sağlıyor.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:white; font-weight: bold;'>Ayrıca, toplam can kaybı sayısı, hafif yaralı sayısı ve ağır yaralı sayısını ilçelere göre sütun grafikleri ile görselleştirdik. Bu grafikler, her ilçenin insan kaybı ve yaralanma risklerini karşılaştırmamıza imkan tanıyor. İlçeler arasındaki farkları belirlememize yardımcı oluyor.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:white; font-weight: bold;'>Son olarak, her ilçenin doğalgaz boru hasarı ve içme suyu boru hasarı değerlerini ilçelere göre görselleştirdik. Bu harita, altyapı hasarının hangi bölgelerde daha yaygın olduğunu göstererek acil müdahale ve onarım gereksinimlerini belirlememize yardımcı oluyor.</span>",
        unsafe_allow_html=True)

    st.write(
        "<span style='color:white; font-weight: bold;'>2.Sayfada İstanbul ilçelerini risk seviyelerine göre üç kümeye ayırdık: Çok Riskli, Orta Riskli ve Riskli. Bu sayfada, her bir ilçenin hangi risk kümelerine ait olduğunu görselleştirdik. Bu analiz, riskli bölgeleri hızlıca tanımlamamıza ve bu bölgelere öncelikli olarak odaklanmamıza yardımcı oluyor.</span>",
        unsafe_allow_html=True)

    # Power BI gömme kodunu gömme
    power_bi_embed_code = """
    <iframe title="sldalmdl" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=7e46c986-67df-4c41-a15a-d29663904a71&autoAuth=true&ctid=fda4d358-3750-4b5b-9588-c0294ccf291e" frameborder="0" allowFullScreen="true"></iframe> """
    st.markdown(power_bi_embed_code, unsafe_allow_html=True)

    st.markdown("<h2 style='color:white; font-weight: bold;font-size:35px;'>Marmara'da Gerçekleşen Depremlerin Ortalama/Toplam Derinlik ve Şiddetleri </h2>",
                unsafe_allow_html=True)

    st.write(
        "<span style='color:white; font-weight: bold;'>İlk görselde, depremlerin enlem ve boylam ölçütlerine göre ortalama derinlik ve ortalama deprem şiddeti değerlerini sunuyoruz. Bu harita ve grafikler, İstanbul'daki deprem aktivitesinin yer altındaki derinlik ve deprem şiddeti açısından nasıl değiştiğini gösteriyor. Bu bilgi, deprem kaynaklarının ve tehlikelerinin daha iyi anlaşılmasına yardımcı olurken, bölgenin daha güvenli bir şekilde planlanması ve yapılandırılması için önemlidir.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:white; font-weight: bold;'>İkinci görselde ise Marmara Bölgesi'nde bulunan şehirlerin deprem aktivitesini incelemeye odaklandık. Bu görsel, Marmara Bölgesi'ndeki farklı şehirlerde meydana gelen ortalama deprem şiddeti ve ortalama derinlik değerlerini sunuyor. Bu bilgiler, Marmara Bölgesi'nde hangi bölgelerin daha fazla deprem etkinliği gösterdiğini anlamamıza yardımcı oluyor. Bu, acil durum hazırlıkları ve risk yönetimi planlarının daha etkili bir şekilde uygulanması için önemli veriler sunmaktadır.</span>",
        unsafe_allow_html=True)
    st.write(
        "<span style='color:white; font-weight: bold;'>Deprem riski ve hazırlık konusundaki farkındalığı artırmak ve bölgelerin daha güvenli bir şekilde planlanmasına katkı sağlamak amacıyla bu analizler yapılmıştır.</span>",
        unsafe_allow_html=True)

    # Power BI gömme kodunu gömme
    power_bi_embed_code = """
    <iframe title="deneme" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=0411cc8e-5617-4e67-9897-0ccff489c4a0&autoAuth=true&ctid=fda4d358-3750-4b5b-9588-c0294ccf291e" frameborder="0" allowFullScreen="true"></iframe> """
    st.markdown(power_bi_embed_code, unsafe_allow_html=True)

    page_by_img = """
          <style>
          [data-testid="stAppViewContainer"]{
          background: url("https://cdn.pixabay.com/photo/2017/08/24/19/41/istanbul-2678082_1280.jpg");
          background-size: cover;top: 0px}

          [data-testid="stHeader"]{
          background-color: rgba(0,0,0,0);
           }

          [data-testid="stToolbar"]{
          right: 2rem;}
          </style>
           """
    st.markdown(page_by_img, unsafe_allow_html=True)
    st.text("")
    st.text("")


def acil_no():
    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Acil Durum Numarları</h2>",unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:25px;'>122 Alo AFAD (Afet ve Acil Durum) </span>",unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:25px;'>112 Ambulans, Polis, Jandarma, İtfaiye</span>",unsafe_allow_html=True)
    page_by_img = """
                   <style>
                   [data-testid="stAppViewContainer"]{
                   background: url("https://cdn.create.vista.com/api/media/small/394838678/stock-photo-damaged-wall-gray-background-crack");
                   background-size: cover;top: 0px}

                   [data-testid="stHeader"]{
                   background-color: rgba(0,0,0,0);
                    }

                   [data-testid="stToolbar"]{
                   right: 2rem;}
                   </style>
                    """
    st.markdown(page_by_img, unsafe_allow_html=True)
    st.text("")


def model():
    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Değerlendirme</h2>",
                unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>Projede modellerimizi değerlendirebilmek için SMAPE yöntemini kullanmayı tercih ettik. SMAPE ölçümünü, kullandığımız modellere göre özelleştirip, detaylandırdık. Önce temel SMAPE fonksiyonumuzu yazdık, daha sonra bu fonksiyonu özelleştirdiğimiz diğer fonksiyonların içerisinde çağırdık. </span>",
        unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:25px;'>Temel SMAPE: </span>",
        unsafe_allow_html=True)
    # PNG resmini yükle
    image = Image.open("1.png")
    # Resmi göster
    st.image(image, use_column_width=True)

    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:25px;'>LightGBM için SMAPE: </span>",
        unsafe_allow_html=True)
    # PNG resmini yükle
    image = Image.open("2.png")
    # Resmi göster
    st.image(image, use_column_width=True)

    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:25px;'>HistGradientBoostingSmape için SMAPE: </span>",
        unsafe_allow_html=True)
    # PNG resmini yükle
    image = Image.open("3.png")
    # Resmi göster
    st.image(image, use_column_width=True)

    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Model Oluşturma</h2>",
                unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>Projemizde Stack/Ensemble Learning yöntemini kullanmayı tercih ettik. Bunun sebebi, oluşacak olan modelin veri setinin varyansına daha fazla hakim olmasını istememizdendir. Bunu şöyle açıklayalım: </span>",
        unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>-HistGradientBossting’in SMAPE değeri: 8.231142277443645</span>",
        unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>-LightGBM’in SMAPE değeri: 9.02614816819916</span>",
        unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>-Ensemble Modelin SMAPE değeri: 4.069787514538628</span>",
        unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>Modeli oluşturma aşamasında; önce LightGBM ve HGBR’i oluşturdum.</span>",
        unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:25px;'>LightGBM:</span>",
        unsafe_allow_html=True)
    # PNG resmini yükle
    image = Image.open("4.png")
    # Resmi göster
    st.image(image, use_column_width=True)

    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:25px;'>HGBR:</span>",
        unsafe_allow_html=True)
    # PNG resmini yükle
    image = Image.open("5.png")
    # Resmi göster
    st.image(image, use_column_width=True)


    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>Problemimiz bir Regresyon Problemi olduğu için VotingRegressor kullanmamız gerekiyordu. Bunu test edebilmemiz için bir fonksiyon yazdık:  </span>",
        unsafe_allow_html=True)
    # PNG resmini yükle
    image = Image.open("6.png")
    # Resmi göster
    st.image(image, use_column_width=True)


    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>Sonucu görebilmek train setlerinizi verdikten sonra modellerinizi de tuple şeklinde vermelisiniz. </span>",
        unsafe_allow_html=True)

    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Alternatif Yol</h2>",
                unsafe_allow_html=True)

    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>Eğer ki elinizde daha önceden eğitilmiş modellerinizin pkl dosyaları varsa, bunları ne yazık ki doğrudan VotingRegressor’un içine yerleştiremiyoruz. VotingRegressor developerları kütüphaneyi tasarlarken sadece instance’ı alabilecek şekilde tasarlamışlar. Bu yüzden alternatif olarak aşağıdaki yolu izleyebilirsiniz: </span>",
        unsafe_allow_html=True)
    # PNG resmini yükle
    image = Image.open("7.png")
    # Resmi göster
    st.image(image, use_column_width=True)



    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Hiperparametre Optimizasyonu</h2>",
                unsafe_allow_html=True)

    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>Zaman Serilerini öğrenmeyi seçip, farklı bir yol izlemeye karar verince farkında olmadığımız bir konu vardı: konunun bitmesinin zaman alacağı… Yaklaşık bir haftalık zamanımızı yiyen Zaman Serileri’nden dolayı modelimizi eğitmede ve fine-tune etmede zaman kaybetmememiz gerekiyordu. İşte bu yüzden Optuna kullanmayı tercih ettik. Optuna’yı hiç bilmeyen için, Random Search’e benzer bir mantık olduğunu söyleyebilirim. Farklı olarak, bir range giriyorsunuz ve bu range arasından değerler Optuna’nın kendisi tarafından rastgele bir şekilde seçiliyor. Ve en güzel tarafı, kaç deneme yapacağınızı kendiniz girebiliyorsunuz. Örneğin ben 5 farklı parametre için rangleri giriyorum. Kabaca her birinde beş değer olsa 3125 adet deneme gerçekleşecek. İşte bize Optuna’nın sağladığı avantaj burada. İstersek 300 istersek 500 deneme yap diyebiliyoruz! Bu da zamandan bize kazandırıyor. Daha fazla zamanınızı almamak adına (ve uzatmamak) LighGBM için tasarladığımız Optuna’nın kodunu aşağıya bırakıyorum. Temel olarak bir fonksiyon yazıyor, daha sonrada bir çalışma (study) nesnesi oluşturuyorsunuz. Minimize argümanını girerek, loss’u en az olan değerin parametresini buluyor:  </span>",
        unsafe_allow_html=True)
    # PNG resmini yükle
    image = Image.open("8.png")
    # Resmi göster
    st.image(image, use_column_width=True)

    # PNG resmini yükle
    image = Image.open("9.png")
    # Resmi göster
    st.image(image, use_column_width=True)

    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Değişken Türetimi</h2>",
                unsafe_allow_html=True)

    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>Zaman Serilerini Makine Öğrenmesi yöntemleri ile kullanacağımız zaman, yapmamız gereken en önemli iş: Veri Setindeki mevsimsellik, trend gibi kavramları ML algoritmasına yedirebilmek. Bunu yapabilmek için en iyi yolumuz Değişken Türetmek. Bizim için hem iyi hem de negatif yönleri olan bu yöntem için kullanacağımız çeşitli yollar var. Negatif diyorum çünkü değişken türetme işini Bağımlı Değişkenin kendisini merkeze alarak yapıyoruz! Bağımlı Değişken’den değişken türetmenin en büyük sorunu overfitting’e yol açabilmesi. Kuracağımız modelin veri setindeki patternı daha iyi öğrenebilmesi için overfitting sorununu kaldırmak adına Random Noise ekledik. Aşşağıdaki fonksiyondan bunu görebilirsiniz: </span>",
        unsafe_allow_html=True)
    # PNG resmini yükle
    image = Image.open("10.png")
    # Resmi göster
    st.image(image, use_column_width=True)

    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Lag Feature Türetimi</h2>",
                unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>Zaman Serisinde geçmiş datayı kullanarak geleceği tahminlemeye çalışıyoruz. Bizim tahminlemeye çalıştığımız Deprem Büyüklüğü (Bağımlı Değişken)’nün geçmiş datasını Python’dan almak ve Random Noise eklemek için aşağıdaki fonksiyonu kullandık: </span>",
        unsafe_allow_html=True)

    # PNG resmini yükle
    image = Image.open("11.png")
    # Resmi göster
    st.image(image, use_column_width=True)

    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Rolling Mean Feature Türetimi</h2>",
                unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>Özellikle Trend’i yakalmak için kullanılan Hareketli Ortalama’yı, aşağıdaki fonksiyon ile türettik. </span>",
        unsafe_allow_html=True)
    # PNG resmini yükle
    image = Image.open("12.png")
    # Resmi göster
    st.image(image, use_column_width=True)


    st.markdown("<h2 style='color:black; font-weight: bold;font-size:35px;'>Exponentially Weighted Mean Feature Türetimi</h2>",
                unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>Mevsimsellik yakalamak için kullanılan Üssel Ağırlıklı Ortalama’yı, aşağıdaki fonksiyon kullanarak türettik.</span>",
        unsafe_allow_html=True)
    # PNG resmini yükle
    image = Image.open("13.png")
    # Resmi göster
    st.image(image, use_column_width=True)


    st.markdown(
        "<h2 style='color:black; font-weight: bold;font-size:35px;'>Time-Based Türetilen Değişkenler</h2>",
        unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>Depremin ne zaman olduğu, akşammı yoksa sabah mı olduğu, hep kış mevsiminde mi gerçekleştiği, belirli çeyreklerde mi oluştuğu, deprem bizi hep uyurken mi yakalıyor gibi soruları sorup analiz edebilmek için DateTime değişkenini kullanarak türettiğimiz değerler: </span>",
        unsafe_allow_html=True)
    # PNG resmini yükle
    image = Image.open("14.png")
    # Resmi göster
    st.image(image, use_column_width=True)


    st.markdown(
        "<h2 style='color:black; font-weight: bold;font-size:35px;'>One Hot Encoding</h2>",
        unsafe_allow_html=True)
    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:17px;'>One Hot Encoding kullanmamızın sebebi, depremin gerçekleştiği yerlerdeki katsayıyı veri setinde etkili bir hale getirebilmek. Bunu istememizin sebebi, ülkemizde 3 fay hattı var ve bu hatların her birinin aktifliği farklı. Örneğin Sakarya’da meydana gelecek olan deprem ile İzmir’de meydana gelecek olan depremin şiddeti birbirinden farklı olacak fay hatlarının özelliklerinden kaynaklı.  Bu yüzden daha önce deprem olan yerlerdeki özellikleri yakalayabilmek için One Hot Encoding kullandık. </span>",
        unsafe_allow_html=True)
    # PNG resmini yükle
    image = Image.open("15.png")
    # Resmi göster
    st.image(image, use_column_width=True)



    st.write(
        "<h2 style='color:black; font-weight: bold;font-size:25px;'></span>",
        unsafe_allow_html=True)
    page_by_img = """
                       <style>
                       [data-testid="stAppViewContainer"]{
                       background: url("https://cdn.create.vista.com/api/media/small/394838678/stock-photo-damaged-wall-gray-background-crack");
                       background-size: cover;top: 0px}

                       [data-testid="stHeader"]{
                       background-color: rgba(0,0,0,0);
                        }

                       [data-testid="stToolbar"]{
                       right: 2rem;}
                       </style>
                        """
    st.markdown(page_by_img, unsafe_allow_html=True)
    st.text("")


# Streamlit uygulamasını başlat
if __name__ == "__main__":
    # Yan taraftaki sidebar düğmeleri
    selected_page = st.sidebar.selectbox("Hangi Sayfaya Gitmek İstersin?", ["Ana Sayfa", "Hakkımızda", "Deprem Nedir?", "Deprem Çeşitleri", "Deprem Ölçümü", "Deprem Güvenliği", "İSTANBUL","Acil Durum Numaraları", "Depremi Nasıl Tahmin Ettik?"])

    if selected_page == "Ana Sayfa":
        main()
    elif selected_page == "Hakkımızda":
        hakkimizda()
    elif selected_page == "Deprem Nedir?":
        deprem_nedir()
    elif selected_page == "Deprem Çeşitleri":
        deprem_cesitleri()
    elif selected_page == "Deprem Ölçümü":
        deprem_olcumu()
    elif selected_page == "Deprem Güvenliği":
        deprem_guvenligi()
    elif selected_page== "İSTANBUL":
        istanbul_özel()
    elif selected_page == "Acil Durum Numaraları":
        acil_no()
    elif selected_page == "Depremi Nasıl Tahmin Ettik?":
        model()

#BUTON
# Streamlit uygulamasını başlat
#if __name__ == "__main__":
    # Yan taraftaki sidebar düğmeleri
 #   if st.sidebar.button("Hakkımızda", key="hakkimizda_button"):
 #       hakkimizda()
  #  if st.sidebar.button("Ana Sayfa", key="ana_sayfa_button"):
  #      main()
   # if st.sidebar.button("Deprem Nedir?", key="deprem_nedir_button"):
   #     deprem_nedir()
  #  if st.sidebar.button("Deprem Çeşitleri", key="deprem_cesitleri_button"):
  #      deprem_cesitleri()
   # if st.sidebar.button("Deprem Ölçümü", key="deprem_olcumu_button"):
    #    deprem_olcumu()
   # if st.sidebar.button("Deprem Güvenliği", key="deprem_guvenligi_button"):
    #    deprem_guvenligi()
    #if st.sidebar.button("Acil Durum Numaraları", key="acil_no_button"):
      #  acil_no()

