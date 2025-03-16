using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace practicSGBD
{
    public partial class Form1 : Form
    {
        private SqlConnection connection;
        private SqlDataAdapter adapterTipFructe;
        private SqlDataAdapter adapterFructe;
        private DataSet dataSet;
        public Form1()
        {
            InitializeComponent();
            InitializeDatabaseConnection();
            LoadTipFructe();
        }
        
        private void InitializeDatabaseConnection()
        {
            string connectionString = System.Configuration.ConfigurationManager.ConnectionStrings["connection"].ConnectionString;
            connection = new SqlConnection(connectionString);
            dataSet = new DataSet();
        }
        
        private void LoadTipFructe()
        {
            string query = "SELECT * FROM TipuriFructe";
            adapterTipFructe = new SqlDataAdapter(query, connection);
            adapterTipFructe.Fill(dataSet, "TipuriFructe");
            
            tipFructeComboBox.DisplayMember = "Tip";
            tipFructeComboBox.ValueMember = "Tid";
            tipFructeComboBox.DataSource = dataSet.Tables["TipuriFructe"];
        }
        
        private void tipFructeComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (tipFructeComboBox.SelectedValue != null)
            {
                int selectedTipFructeId = (int)tipFructeComboBox.SelectedValue;
                LoadFructe(selectedTipFructeId);
            }
        }

        private void LoadFructe(int tipFructeId)
        {
            string query = $"SELECT * FROM Fructe WHERE Tid = {tipFructeId}";
            adapterFructe = new SqlDataAdapter(query, connection);

            if (dataSet.Tables.Contains("Fructe"))
            {
                dataSet.Tables["Fructe"].Clear();
            }

            adapterFructe.Fill(dataSet, "Fructe");

            if (dataSet.Tables["Fructe"].Rows.Count > 0)
            {
                fructeGridView.DataSource = dataSet.Tables["Fructe"];
            }
            else
            {
                fructeGridView.DataSource = null;
            }
        }
        
        private void gridViewFructe_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex >= 0)
            {
                DataGridViewRow row = this.fructeGridView.Rows[e.RowIndex];
                fidTextBox.Text = row.Cells["Fid"].Value.ToString();
                denumireTextBox.Text = row.Cells["Denumire"].Value.ToString();
                culoareTextBox.Text = row.Cells["Culoare"].Value.ToString();
                lunaOptimaTextBox.Text = row.Cells["LunaOptimaCulegere"].Value.ToString();
                pretMediuTextBox.Text = row.Cells["PretMediu"].Value.ToString();
                tidTextBox.Text = row.Cells["Tid"].Value.ToString();
            }
        }
        
        private void adaugaButton_Click(object sender, EventArgs e)
        {
            adapterFructe.InsertCommand = new SqlCommand("INSERT INTO Fructe VALUES (@Denumire, @Culoare, @LunaOptimaCulegere, @PretMediu, @Tid)", connection);
            adapterFructe.InsertCommand.Parameters.AddWithValue("@Denumire", denumireTextBox.Text);
            adapterFructe.InsertCommand.Parameters.AddWithValue("@Culoare", culoareTextBox.Text);
            adapterFructe.InsertCommand.Parameters.AddWithValue("@LunaOptimaCulegere", lunaOptimaTextBox.Text);
            adapterFructe.InsertCommand.Parameters.AddWithValue("@PretMediu", pretMediuTextBox.Text);
            adapterFructe.InsertCommand.Parameters.AddWithValue("@Tid", tidTextBox.Text);
            
            connection.Open();
            adapterFructe.InsertCommand.ExecuteNonQuery();
            connection.Close();
            
            dataSet.Clear();
            adapterFructe.Fill(dataSet, "Fructe");
            MessageBox.Show("Fruct adaugat cu succes!");
        }
        
        private void buttonSterge_Click(object sender, EventArgs e)
        {
                adapterFructe.DeleteCommand = new SqlCommand("DELETE FROM Fructe WHERE Fid = @Fid", connection);
                adapterFructe.DeleteCommand.Parameters.AddWithValue("@Fid", fidTextBox.Text);

                connection.Open();
                adapterFructe.DeleteCommand.ExecuteNonQuery();
                connection.Close();

                dataSet.Clear();
                adapterFructe.Fill(dataSet, "Fructe");
                MessageBox.Show("Fruct sters cu succes!");
            
            
        }
        
        private void buttonModifica_Click(object sender, EventArgs e)
        {
            
                adapterFructe.UpdateCommand = new SqlCommand("UPDATE Fructe SET Denumire = @Denumire, Culoare = @Culoare, LunaOptimaCulegere = @LunaOptimaCulegere, PretMediu = @PretMediu, Tid = @Tid WHERE Fid = @Fid", connection);
                adapterFructe.UpdateCommand.Parameters.AddWithValue("@Fid", fidTextBox.Text);
                adapterFructe.UpdateCommand.Parameters.AddWithValue("@Denumire", denumireTextBox.Text);
                adapterFructe.UpdateCommand.Parameters.AddWithValue("@Culoare", culoareTextBox.Text);
                adapterFructe.UpdateCommand.Parameters.AddWithValue("@LunaOptimaCulegere", lunaOptimaTextBox.Text);
                adapterFructe.UpdateCommand.Parameters.AddWithValue("@PretMediu", pretMediuTextBox.Text);
                adapterFructe.UpdateCommand.Parameters.AddWithValue("@Tid", tidTextBox.Text);
        
                connection.Open();
                adapterFructe.UpdateCommand.ExecuteNonQuery();
                connection.Close();
        
                dataSet.Clear();
                adapterFructe.Fill(dataSet, "Fructe");
                MessageBox.Show("Fruct modificat cu succes!");
            
        }

    }
    
}