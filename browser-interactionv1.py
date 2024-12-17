import streamlit as st
import graphviz

# Set Streamlit app configurations
st.set_page_config(
    page_title="Browser Interaction Workflow",
    layout="wide"
)

# App Title
st.title("Internet Browser Interaction with Domains")
st.markdown("""
This application explains how internet browsers interact with **new website domains** and **currently indexed domains**.
""")

# Section 1: Workflow Summary
st.header("Workflow Overview")
st.markdown("""
When a user enters a website's domain name in a browser, a series of steps take place to resolve the domain and display the webpage. These steps are:
1. **DNS Resolution**: Converts the domain name into an IP address.
2. **Connection Establishment**: Sets up a secure communication channel using protocols like TCP and HTTPS.
3. **Webpage Request**: Fetches the HTML and other resources (CSS, JS, images).
4. **Caching and Rendering**: Optimizes performance and displays the webpage.
5. **Search Engine Interaction**: Handles how new and indexed domains are processed differently.
""")

# Section 2: Detailed Steps with Expanders
st.header("Detailed Steps")

with st.expander("Step 1: DNS Resolution"):
    st.markdown("""
    - **New Website Domain**: The browser queries root DNS servers, TLD servers, and authoritative nameservers to resolve the IP address.
    - **Indexed Website Domain**: The IP address is retrieved from cached DNS records.
    """)

with st.expander("Step 2: Connection Establishment"):
    st.markdown("""
    - A TCP connection is established to the resolved IP address.
    - For secure connections, an HTTPS handshake is performed using TLS.
    """)

with st.expander("Step 3: Webpage Request"):
    st.markdown("""
    - The browser sends an HTTP GET request to fetch the webpage and associated resources (CSS, JS, images).
    """)

with st.expander("Step 4: Caching and Rendering"):
    st.markdown("""
    - Resources like HTML, CSS, and images are cached locally for faster future access.
    - The browser uses these resources to render the webpage.
    """)

with st.expander("Step 5: Search Engine Interaction"):
    st.markdown("""
    - **New Website Domain**: Search engines crawl and index the site.
    - **Indexed Website Domain**: Cached versions of the site are used for faster retrieval.
    """)

# Section 3: Diagram
st.header("Diagram: Browser Interaction Workflow")

# Create a Graphviz diagram
diagram = graphviz.Digraph(format="svg")
diagram.attr(rankdir="TB", size="8,6")

# Diagram Nodes
diagram.node("UserInput", "User Inputs Domain Name")
diagram.node("DNSResolution", "DNS Resolution")
diagram.node("Connection", "Connection Establishment\n(TCP/HTTPS)")
diagram.node("Request", "Webpage Request\n(HTTP GET)")
diagram.node("Caching", "Caching & Rendering\n(Local Optimization)")
diagram.node("SearchEngine", "Search Engine Interaction")

# Diagram Edges
diagram.edges([
    ("UserInput", "DNSResolution"),
    ("DNSResolution", "Connection"),
    ("Connection", "Request"),
    ("Request", "Caching"),
    ("Request", "SearchEngine")
])

# Render the diagram
st.graphviz_chart(diagram)

# Section 4: Key Differences Table
st.header("Key Differences Between New and Indexed Domains")

st.markdown("""
| Aspect                  | New Website Domain                                  | Indexed Website Domain                           |
|-------------------------|----------------------------------------------------|-------------------------------------------------|
| **DNS Resolution**      | Slower; involves querying DNS servers.             | Faster; often resolved from cached records.     |
| **Caching**             | Minimal or no caching.                             | Extensive caching for faster loading.           |
| **Search Discovery**    | Not yet discoverable in search results.            | Easily discoverable in search results.          |
| **Error Likelihood**    | Higher (e.g., misconfigurations).                  | Lower (stable and optimized).                   |
| **Security Warnings**   | More likely if SSL/TLS is missing.                 | Less likely due to established configurations.  |
""")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using [Streamlit](https://streamlit.io).")

