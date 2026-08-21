import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

import numpy as np
import pandas as pd
import streamlit as st
from stock.models import Product

st.title("📊 Painel de Detalhes do Produto")


def dashboard():
  produto_id = st.query_params.get("product_id")

  if not produto_id:
    st.warning("Nenhum produto foi selecionado.")
    return

  try:
    produto = Product.objects.get(id=produto_id)
    preco_atual = produto.price

    st.write(f"**Produto:** {produto.name_product}")
    st.write(f"**Preço:** R$ {preco_atual}")

    chart_data = pd.DataFrame(
        np.random.randn(13, 3),
        columns=["quantidades", "preço", "vendas"],
    )

    st.line_chart(chart_data)

  except Product.DoesNotExist:
    st.error("Produto não encontrado no banco de dados.")


dashboard()