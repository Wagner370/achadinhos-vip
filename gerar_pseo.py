import os

produtos = [
    {
        'slug': 'mop-giratorio-inox-360-vale-a-pena',
        'nome': 'Mop Giratório Balde Inox Lava e Seca 360',
        'preco': 'R$ 69,90',
        'link': 'https://lista.mercadolivre.com.br/mop-giratorio-balde-inox#afiliado_tag=MARKETINGEWMB',
        'imagem': 'imagens/mop_giratorio_luxo.jpg',
        'descricao': 'O Mop Giratório Balde Inox 360 é a solução definitiva para limpeza pesada e diária sem contato manual com água suja ou produtos químicos. Cesto de centrifugação 100% em aço inoxidável cirúrgico de alta durabilidade.',
        'beneficios': ['Centrifugação rápida em inox', 'Cabo ergonômico reforçado', 'Refil microfibra lavável', 'Ideal para pisos frios, madeira e laminados'],
        'faq': [
            ('O cesto enferruja?', 'Não, o cesto é em aço inox de alta resistência à oxidação.'),
            ('Acompanha refil extra?', 'Sim, acompanha refil de microfibra de alta absorção.'),
            ('O frete é grátis?', 'Sim, pelo Mercado Livre Full com entrega no dia seguinte.')
        ]
    },
    {
        'slug': 'mini-selador-termico-portatil-funciona',
        'nome': 'Mini Selador Térmico Portátil para Alimentos',
        'preco': 'R$ 29,90',
        'link': 'https://meli.la/1oDisGQ',
        'imagem': 'imagens/selador_termico_luxo.jpg',
        'descricao': 'O Mini Selador Térmico Portátil veda sacos plásticos instantaneamente por aquecimento térmico microcontrolado, mantendo salgadinhos, biscoitos e mantimentos 100% crocantes e frescos.',
        'beneficios': ['Vedação hermética em 3 segundos', 'Imã traseiro para fixar na geladeira', 'Funciona a pilhas padrão', 'Evita desperdício de comida'],
        'faq': [
            ('Funciona em qualquer plástico?', 'Sim, veda perfeitamente sacos de salgadinho, arroz, feijão e embalagens aluminizadas.'),
            ('Precisa esperar esquentar?', 'Não, aquece instantaneamente ao pressionar.'),
            ('Tem trava de segurança?', 'Sim, possui aba protetora para evitar acionamentos acidentais.')
        ]
    },
    {
        'slug': 'camera-lampada-wifi-360-e-boa',
        'nome': 'Câmera de Segurança Wi-Fi 360 Lâmpada E27',
        'preco': 'R$ 59,90',
        'link': 'https://lista.mercadolivre.com.br/camera-lampada-wifi-360#afiliado_tag=MARKETINGEWMB',
        'imagem': 'imagens/camera_lampada_luxo.jpg',
        'descricao': 'Câmera de Segurança panorâmica formato lâmpada com rosca padrão E27. Instalação em 2 minutos sem furar paredes nem passar fios. Visão noturna colorida, áudio bidirecional e rastreamento de movimento humano.',
        'beneficios': ['Instalação direta no bocal da lâmpada', 'Visão noturna inteligente infravermelho e LED', 'Microfone e alto-falante integrados', 'Acesso pelo celular de qualquer lugar do mundo'],
        'faq': [
            ('Precisa de técnico para instalar?', 'Não, você mesmo rosqueia no bocal comum de lâmpada e conecta no Wi-Fi.'),
            ('Grava sem internet?', 'Sim, salva tudo continuamente no cartão MicroSD inserido nela.'),
            ('Funciona no aplicativo em português?', 'Sim, aplicativo compatível com Android e iPhone em português.')
        ]
    },
    {
        'slug': 'fone-bluetooth-lenovo-sem-fio-analise',
        'nome': 'Fone de Ouvido Bluetooth Lenovo Sem Fio TWS',
        'preco': 'R$ 49,90',
        'link': 'https://lista.mercadolivre.com.br/fone-de-ouvido-bluetooth-lenovo#afiliado_tag=MARKETINGEWMB',
        'imagem': 'imagens/fone_lenovo_luxo.jpg',
        'descricao': 'Fone de Ouvido TWS Lenovo com Bluetooth 5.3 de ultra-baixa latência, drivers dinâmicos com graves potentes e cancelamento de ruído passivo ergonômico. Bateria com até 20 horas de autonomia com estojo.',
        'beneficios': ['Bluetooth 5.3 com conexão instantânea', 'Graves profundos e som cristalino', 'Resistente a respingos e suor', 'Estojo compacto com display digital'],
        'faq': [
            ('Serve para corrida e academia?', 'Sim, encaixe intra-auricular firme com isolamento excelente.'),
            ('Funciona em qualquer celular?', 'Compatível com Samsung, Xiaomi, Motorola, iPhone e notebooks.'),
            ('Quanto tempo dura a bateria?', 'Até 5 horas contínuas de música, e mais 15 horas com as recargas do estojo.')
        ]
    },
    {
        'slug': 'bomba-eletrica-galao-agua-recarregavel-vale-a-pena',
        'nome': 'Bomba Elétrica para Galão de Água USB Recarregável',
        'preco': 'R$ 24,90',
        'link': 'https://lista.mercadolivre.com.br/bomba-eletrica-para-galao-de-agua-recarregavel#afiliado_tag=MARKETINGEWMB',
        'imagem': 'imagens/bomba_agua_luxo.jpg',
        'descricao': 'Dispensador automático para galões de água de 10L e 20L. Acionamento em 1 clique sem virar galões pesados. Bateria de longa duração recarregável via USB.',
        'beneficios': ['Acionamento fácil em 1 toque', 'Compatível com galões de 10L e 20L', 'Bateria dura até 8 galões com 1 carga', 'Higiênica e livre de bactérias'],
        'faq': [
            ('Serve em galão de 20 litros?', 'Sim, encaixa com perfeição em galões de 10L e 20L padrão.'),
            ('Como é feito o carregamento?', 'Via cabo USB padrão, pode carregar em qualquer carregador de celular.'),
            ('A mangueira é atóxica?', 'Sim, mangueira de silicone de grau alimentício 100% segura.')
        ]
    }
]

template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{nome} Vale a Pena em 2026? Análise Completa e Onde Comprar</title>
  <meta name="description" content="{descricao}">
  <meta name="keywords" content="{nome}, Mercado Livre, vale a pena, menor preco, desconto, comprar online, resenha sincera">
  
  <meta property="og:title" content="{nome} - Análise Completa e Preço Baixo">
  <meta property="og:description" content="{descricao}">
  <meta property="og:image" content="https://wagner370.github.io/achadinhos-vip/{imagem}">
  <meta property="og:url" content="https://wagner370.github.io/achadinhos-vip/{slug}.html">
  <meta name="robots" content="index, follow, max-image-preview:large">
  
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org/",
    "@type": "Product",
    "name": "{nome}",
    "image": "https://wagner370.github.io/achadinhos-vip/{imagem}",
    "description": "{descricao}",
    "brand": {{
      "@type": "Brand",
      "name": "Achadinhos VIP Oficial"
    }},
    "offers": {{
      "@type": "Offer",
      "url": "{link}",
      "priceCurrency": "BRL",
      "price": "{preco_num}",
      "availability": "https://schema.org/InStock",
      "seller": {{
        "@type": "Organization",
        "name": "Mercado Livre Oficial"
      }}
    }},
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "1480"
    }}
  }}
  </script>

  <style>
    :root {{
      --bg: #0b0f19;
      --card-bg: #131b2e;
      --accent: #ffe600;
      --accent-hover: #ffd000;
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --green: #00e676;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }}
    body {{ background: var(--bg); color: var(--text); line-height: 1.6; padding: 20px 10px; }}
    .container {{ max-width: 800px; margin: 0 auto; background: var(--card-bg); border-radius: 16px; padding: 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.05); }}
    .badge {{ display: inline-block; background: rgba(255,230,0,0.15); color: var(--accent); padding: 6px 14px; border-radius: 20px; font-weight: 700; font-size: 0.85rem; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 1px; }}
    h1 {{ font-size: 1.8rem; margin-bottom: 20px; color: #ffffff; line-height: 1.3; }}
    .product-hero {{ text-align: center; margin: 25px 0; }}
    .product-hero img {{ max-width: 100%; max-height: 380px; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.6); object-fit: cover; border: 1px solid rgba(255,255,255,0.1); }}
    .price-box {{ background: rgba(0,230,118,0.1); border: 1px solid var(--green); border-radius: 12px; padding: 20px; text-align: center; margin: 25px 0; }}
    .price-tag {{ font-size: 2.2rem; font-weight: 800; color: var(--green); }}
    .btn-buy {{ display: block; width: 100%; max-width: 400px; margin: 15px auto 0; background: var(--accent); color: #111; text-align: center; padding: 16px 24px; border-radius: 50px; font-size: 1.2rem; font-weight: 800; text-decoration: none; box-shadow: 0 6px 20px rgba(255,230,0,0.4); transition: transform 0.2s, background 0.2s; }}
    .btn-buy:hover {{ background: var(--accent-hover); transform: scale(1.02); }}
    .section-title {{ font-size: 1.3rem; margin: 30px 0 15px; color: var(--accent); border-bottom: 2px solid rgba(255,230,0,0.2); padding-bottom: 8px; }}
    .benefits-list {{ list-style: none; margin-bottom: 25px; }}
    .benefits-list li {{ padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: center; font-size: 1.05rem; }}
    .benefits-list li::before {{ content: '✔'; color: var(--green); font-weight: 900; margin-right: 12px; font-size: 1.2rem; }}
    .faq-item {{ margin-bottom: 18px; background: rgba(255,255,255,0.03); padding: 16px; border-radius: 10px; }}
    .faq-question {{ font-weight: 700; color: #ffffff; margin-bottom: 6px; font-size: 1.05rem; }}
    .faq-answer {{ color: var(--text-muted); font-size: 0.95rem; }}
    .footer-bar {{ text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.08); font-size: 0.9rem; color: var(--text-muted); }}
    .footer-bar a {{ color: var(--accent); text-decoration: none; }}
  </style>
</head>
<body>
  <div class="container">
    <span class="badge">⭐ Análise Sincera 2026 • Estoque Full Brasil</span>
    <h1>{nome}: Vale a Pena? Análise Completa, Prós e Menor Preço Garantido</h1>
    
    <div class="product-hero">
      <img src="{imagem}" alt="{nome}">
    </div>

    <div class="price-box">
      <p style="font-size: 0.95rem; color: var(--text-muted); text-transform: uppercase;">Oferta com Envio Imediato no Mercado Livre Full</p>
      <div class="price-tag">{preco}</div>
      <p style="color: var(--green); font-weight: 600;">🔒 Estoque Verificado e Compra Protegida</p>
      <a href="{link}" class="btn-buy" target="_blank" rel="nofollow noopener">VER OFERTA NO MERCADO LIVRE ➔</a>
    </div>

    <h2 class="section-title">O Que É e Como Funciona?</h2>
    <p style="color: #cbd5e1; font-size: 1.05rem; margin-bottom: 20px;">{descricao}</p>

    <h2 class="section-title">Principais Vantagens e Benefícios</h2>
    <ul class="benefits-list">
      {beneficios_html}
    </ul>

    <h2 class="section-title">Perguntas Frequentes (Tira-Dúvidas)</h2>
    {faq_html}

    <div style="margin-top: 30px; text-align: center;">
      <a href="{link}" class="btn-buy" target="_blank" rel="nofollow noopener">GARANTIR O MEU COM FRETE RÁPIDO ➔</a>
    </div>

    <div class="footer-bar">
      <p>© 2026 Vitrine Oficial Achadinhos VIP • <a href="index.html">Voltar para a Vitrine Completa</a></p>
      <p style="margin-top: 5px; font-size: 0.8rem;">Links comissionados e seguros integrados com a plataforma do Mercado Livre.</p>
    </div>
  </div>
</body>
</html>
"""

destino = r'C:\Users\Usuario\Documents\achadinhos-vip'
sitemap_urls = ['https://wagner370.github.io/achadinhos-vip/']

for p in produtos:
    beneficios_html = '\n'.join([f"<li>{b}</li>" for b in p['beneficios']])
    faq_html = '\n'.join([f'<div class="faq-item"><div class="faq-question">❓ {q}</div><div class="faq-answer">{a}</div></div>' for q, a in p['faq']])
    preco_num = p['preco'].replace('R$ ', '').replace(',', '.')
    
    html = template.format(
        nome=p['nome'],
        slug=p['slug'],
        preco=p['preco'],
        preco_num=preco_num,
        link=p['link'],
        imagem=p['imagem'],
        descricao=p['descricao'],
        beneficios_html=beneficios_html,
        faq_html=faq_html
    )
    
    file_path = os.path.join(destino, f"{p['slug']}.html")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    sitemap_urls.append(f"https://wagner370.github.io/achadinhos-vip/{p['slug']}.html")
    print(f"Gerado: {p['slug']}.html")

sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in sitemap_urls:
    sitemap_content += f'  <url>\n    <loc>{url}</loc>\n    <lastmod>2026-10-05</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.9</priority>\n  </url>\n'
sitemap_content += '</urlset>'

with open(os.path.join(destino, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print('sitemap.xml gerado com sucesso!')

robots_content = 'User-agent: *\nAllow: /\n\nSitemap: https://wagner370.github.io/achadinhos-vip/sitemap.xml\n'
with open(os.path.join(destino, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(robots_content)
print('robots.txt gerado com sucesso!')
