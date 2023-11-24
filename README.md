# `ai-phishing-check`

AI Phishing Check, Python dili kullanılarak geliştirilmiş bir **Yapay Zeka** projesidir. Bu proje, phishing saldırılarını tespit etmek amacıyla eğitilmiş bir yapay zeka modeli içerir.

## Kurulum

- Projeyi yerel bilgisayarınıza klonlayın:

```bash
git clone https://github.com/AbdullahDalgic/ai-phishing-check.git
cd ai-phishing-check
```

- Proje için gereksinimleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

```bash
pip3 -U -r requirements.txt
```

**NOT:** Eğer Python yüklü değilse, önce [Python'u indirip yüklemeniz gerekmektedir.](https://www.python.org/downloads/)

## Kullanım

Projenin başlatılması için aşağıdaki komutu kullanmalısınız:

```bash
py ./phishing.py
```

Proje, ilk çalıştırıldığında otomatik olarak eğitim verisi üzerinden modeli oluşturacak ve ardından program otomatik olarak çalışmaya başlayacaktır. Daha sonraki çalıştırmalarda ise var olan model kullanılacaktır, tekrar model oluşturmaya gerek kalmayacaktır.

## Veri Seti ve Model

Proje içerisinde dataset klasörü eğitim verilerini içerirken, model klasörü eğitilmiş modelin dosyasını içerir. İlk çalıştırmada model dosyası bulunmaz ancak program otomatik olarak modeli eğitir. Daha sonraki çalıştırmalarda ise var olan model kullanılır.

## Lisans

Bu proje açık kaynaklıdır ve sadece eğitim amaçlıdır. MIT lisansı altında dağıtılmaktadır.

## Katkıda Bulunma

Eğer projeye katkıda bulunmak istiyorsanız, lütfen bir konu açın veya bir çekme isteği gönderin. Katkılarınızı bekliyoruz!
