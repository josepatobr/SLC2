import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

import django
django.setup()

import numpy as np
import pandas as pd
import streamlit as st
from stock.models import Product, StockMovement

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

    st.write(f"**Produto:** {produto.name_product}")
    st.write(f"**Preço:** R$ {price}")


    st.write("planilha focada no armazenamento do produto")

    quantity_table = []
    for v in vendas:
        data_mov = pd.to_datetime(v.date_moved)
        quantity_table.append({
                'Data': data_mov,
                'Mes': data_mov.strftime('%b').capitalize(), 
                'Vendas': v.quantity_out,
                'Estoque': produto.stock_quantity
            })

    st.write("planilha focada na economia do produto")


    economy_table = []
    for v in vendas: 
      economy_table.append({
        'Vendas': v.quantity_out,
        'lucros': v.profits,
        'gastos com o reabastecemento': produto.price_restocking,
        })
      if not v.profits:
        st.error("erro ao mostrar o lucro")

       

    st.bar_chart(quantity_table)
    st.line_chart(economy_table)


  except Product.DoesNotExist:
    st.error("Produto não encontrado no banco de dados.")


dashboard()