const express = require('express');
const app = express();
const PORT = 3001;

app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET,POST');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
});

app.get('/jenkins/builds', async (req, res) => {
    // Usa import() dinámico para cargar node-fetch solo cuando sea necesario
    const fetch = (await import('node-fetch')).default;
    
    try {
        const response = await fetch('http://localhost:8085/job/work-test/api/json?tree=builds[number,url]{0,1}', {
            headers: {
                'Authorization': 'Basic ' + Buffer.from('cberreta:112a10c0315893eb0af25d88054e43d50').toString('base64')
            }
        });
        
        if (!response.ok) throw new Error('Error al obtener los datos de Jenkins');
        
        const data = await response.json();
        res.json(data);
    } catch (error) {
        console.error("Error al conectarse con Jenkins:", error);
        res.status(500).json({ error: 'Error al obtener datos de Jenkins' });
    }
});

app.listen(PORT, () => {
    console.log(`Proxy server running on http://localhost:${PORT}`);
});
