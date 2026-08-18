# Ganga Residency Website

Starter website for **Ganga Residency** — a 15 acre plotted township in Garhmukteshwar.

**Live domain:** [www.gangaresidency.co.in](https://www.gangaresidency.co.in)

## Enable contact forms (required)

Forms use [Web3Forms](https://web3forms.com). Without a valid access key, submit fails with:

`Invalid form_id/access_key format. Must be a valid UUID.`

**Setup:**

1. Open https://web3forms.com
2. Enter the email where you want lead notifications
3. Copy the **Access Key** (UUID format)
4. Paste it in `docs/site-config.js`:

```javascript
web3formsAccessKey: "your-uuid-here",
```

5. Redeploy the site

You can reuse the same Web3Forms key as Ganga County if leads go to the same inbox — just paste that UUID here.

## Local preview

```bash
cd docs && python3 -m http.server 8080
```

Open http://localhost:8080
