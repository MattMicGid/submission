import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu

data = pd.read_csv('main_data.csv')

def plot_customer_by_state(data):
    bystate_df = data.groupby(by="customer_state").customer_id.nunique().reset_index()
    bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

    plt.figure(figsize=(10, 5))
    sns.barplot(x="customer_count", y="customer_state",
                data=bystate_df.sort_values(by="customer_count", ascending=False),
                palette='viridis')
    plt.title("Number of buy by States", loc="center", fontsize=15)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='y', labelsize=12)
    st.pyplot(plt)

def plot_top_product_categories(data):
    sp_product_categories = data.loc[data['customer_state'] == "SP", 'product_category_name_english']
    sp_product_category_counts = sp_product_categories.value_counts().reset_index()
    sp_product_category_counts.columns = ['product_category_name_english', 'count']
    top_10_product_categories = sp_product_category_counts.head(10)

    plt.figure(figsize=(10, 5))
    sns.barplot(x='count', y='product_category_name_english',
                data=top_10_product_categories.sort_values(by='count', ascending=False),
                palette='viridis')
    plt.title("Top 10 Product Categories in São Paulo", loc="center", fontsize=15)
    plt.ylabel("Product Category")
    plt.xlabel("Number of Products")
    plt.tick_params(axis='y', labelsize=12)
    st.pyplot(plt)

def plot_payment_type_distribution():
    payment_type_counts = [77198, 19910, 5830, 1536]
    payment_types = ['credit_card', 'boleto', 'voucher', 'debit_card']

    plt.figure(figsize=(8, 8))
    plt.pie(payment_type_counts, labels=payment_types, autopct='%1.1f%%', colors=plt.cm.tab10.colors)
    plt.title('Payment Type Distribution')
    plt.axis('equal')  
    st.pyplot(plt)

def plot_mean_review_score_by_payment_type():
    payment_types = ['debit_card', 'credit_card', 'boleto', 'voucher']
    mean_review_scores = [4.168084, 4.087637, 4.086631, 4.003804]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=mean_review_scores, y=payment_types, palette='viridis')
    plt.xticks(ticks=range(6), labels=range(6))
    plt.title('Mean Review Score by Payment Type')
    plt.xlabel('Mean Review Score')
    plt.ylabel('Payment Type')
    st.pyplot(plt)

st.header('Dashboard E-Commerce')

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "question1", "question2"],
        icons=["house", "patch-question", "patch-question"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    st.title(f"Proyek analisis data")
    st.subheader("About Me:")
    st.text("Nama: Matthew Michael Gideon")
    st.text("Email: mattmicgid@gmail.com")
    st.text("ID Dicoding: mattmicgid")
    st.subheader("Project Overview")
    st.text("Proyek ini merupakan proyek akhir dari proyek analisis data dengan tujuan menganalisis")
    st.text("data yang diberikan dan kita visualisasikan yang kemudian kita masukkan ke dalam dashboard.")
    st.subheader("Pertanyaan bisnis:")
    st.text("Dimana pembelian terbanyak pada masing-masing negara bagian dan produk dengan kategori")
    st.text("apa yang paling sering dibeli pada negara bagian dengan pembelian terbanyak.")
    st.text("Bagaimana korelasi antara jenis pembayaran pengguna dengan tingkat kepuasan pengguna")
    st.text("dalam data E-Commerce tersebut.")
    st.caption('Matthew Michael Gideon')



if selected == "question1":
    st.title(f"Pertanyaan ke 1")
    st.subheader('Dimana pembelian terbanyak pada masing-masing negara bagian dan produk dengan kategori apa yang paling sering dibeli pada negara bagian dengan pembelian terbanyak')
    st.subheader("Berikut merupakan pembelian terbanyak pada masing-masing negara bagian")
    plot_customer_by_state(data)
    with st.expander("See explanation"):
        st.write("Dapat diketahui bahwa diatas menunjukkan SP yang berada pada peringkat paling atas yang menunjukkan bahwa Sao Paulo merupakan pembeli terbanyak dilanjuti dengan RJ / Rio de Janeiro dan dilanjuti dengan MG / Minas Geiras")
    st.subheader('Jenis kategori barang dengan pembelian terbanyak pada Sao Paulo yang merupakan negara bagian dengan pembelian terbanyak')
    plot_top_product_categories(data)
    with st.expander("See explanation"):
        st.write("Jenis kategori barang dengan pembelian terbanyak pada Sao Paulo yang merupakan negara bagian dengan pembelian terbanyak pada kategori bed_bath_table")

if selected == "question2":
    st.title(f"Pertanyaan Ke 2")
    st.subheader('Bagaimana korelasi antara jenis pembayaran pengguna dengan tingkat kepuasan pengguna dalam data E-Commerce tersebut')
    st.subheader("Persentase penggunaan jenis-jenis pembayaran")
    plot_payment_type_distribution()
    
    st.subheader('Rata-rata nilai review dengan jenis pembayaran')
    plot_mean_review_score_by_payment_type()
    with st.expander("See explanation"):
        st.write("Dapat diketahui bahwa nilai review pada masing-masing pembayaran memiliki nilai satisfaksi lebih dari 4 sehingga ini membuktikan bahwa pengguna sangat senang dengan jenis-jenis pembayaran")
