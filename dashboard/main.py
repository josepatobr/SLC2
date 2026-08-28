import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

import django
django.setup()

import streamlit as st
from stock.models import Product, StockMovement, Seller, Company
import streamlit.components.v1 as components


st.title("📊 Painel de Detalhes do Produto")


def dashboard():
  produto_id = st.query_params.get("product_id")

  if not produto_id:
    st.warning("o produto não foi encontrado.")
    return

  try:
    produto = Product.objects.get(id=produto_id)

    vendas = StockMovement.objects.filter(product_id=produto_id).order_by("date_moved")
    if not vendas.exists():
        st.info("Ainda não há movimentações registradas para este produto.")
        return

    price = produto.price


    components.html(
        f"""
        <div style="font-size: 50px; color:white; justify-content: center; text-align: center; underline: underline;
        ">
          {produto.name_product}
        </div>  
        """,
        height=100,
    )


    st.markdown("---")


    components.html(
        f"""
        <div style="color: white; font-size: 20px; color:white; justify-content: center; text-align: center
        ">
          planilha focada no armazenamento do produto
        </div>  
        """,
        height=50,
    )


    #Dados de vendas e estoque para o gráfico
    vendas = ["10", "20", "30", "40", "50", "60", "70", "80", "90",  ]
    estoque = ["100", "90", "80", "70", "60", "50", "40", "30", "20", ]
    data = ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01',  '2023-07-01', '2023-08-01', '2023-09-01', '2023-10-01', ]
    mes = ['mes 1', 'mes 2', 'mes 3', 'mes 4', 'mes 5', 'mes 6', 'mes 7', 'mes 8', 'mes 9',]

    quantity_table = []
    for i in range(len(vendas)):
        quantity_table.append({
            'Mes': mes[i], 
            'Vendas obtidas': int(vendas[i]),
            'Estoque restante': int(estoque[i])
        })

    st.bar_chart(quantity_table, x='Mes', y=['Vendas obtidas', 'Estoque restante'])


    st.markdown("---")


    components.html(
        f"""
        <div style="color: white; font-size: 20px; color:white; justify-content: center; text-align: center
        ">
          planilha focada na economia do produto
        </div>  
        """,
        height=50,
    )


    Vendas = ["10", "20", "30", "40", "50", "60", "70", "80", "90"]
    lucros = ["100", "200", "300", "400", "500", "600", "700", "800", "900"]
    gastos_reabastecimento = ["50", "100", "150", "200", "250", "300", "350", "400", "450"]
    mes = ['mes 1', 'mes 2', 'mes 3', 'mes 4', 'mes 5', 'mes 6', 'mes 7', 'mes 8', 'mes 9']

    totais = []

    for i in range(len(lucros)):
        subtracao = int(lucros[i]) - int(gastos_reabastecimento[i])
        totais.append(subtracao)

    economy_table = []
    for i in range(len(vendas)):
      economy_table.append({
        'Mes': mes[i], 
        'Vendas': int(Vendas[i]),
        'lucros': int(lucros[i]),
        'gastos': int(gastos_reabastecimento[i]),
        'Total': int(totais[i])  
      })

    st.line_chart(economy_table, x='Mes', y=['Vendas', 'lucros', 'gastos', 'Total'])


    #falta arrumar isso
    components.html(
      f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 50px;">
          <a href="/dashboard/details?product_id={produto_id}" 
            style="color: white; background-color: gray; padding: 10px 20px; border-radius: 5px;">
            Mais detalhes sobre a data da venda
          </a>
        </div>
      """,
      height=70,
    )
    


    seller = Seller.objects.filter(id=produto.seller_id).first()
    company = Company.objects.filter(id=produto.company_id).first()

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: gray;'>© 2026 - Informações do Produto</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"**Vendedor:** {seller.name}  \n **Email:** {seller.email}  \n **Empresa:** {company.name}")

    with col2:
        st.markdown(f"**Empresa:** {company.name}  \n **Telefone:** {company.number}  \n **Endereço:** {company.ender}")
  except Product.DoesNotExist:
    st.error("Produto não encontrado no banco de dados.")


dashboard()