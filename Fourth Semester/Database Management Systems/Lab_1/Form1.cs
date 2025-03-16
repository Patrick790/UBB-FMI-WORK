using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.Windows.Markup;
using System.Net.NetworkInformation;

namespace Lab_1
{
    public partial class midTextBox : Form
    {

        SqlConnection connection = new SqlConnection(@"Data Source=PatricksYoga7\SQLEXPRESS; Initial Catalog=EchipaDeHandbal3;Integrated Security=true");

        SqlDataAdapter dataAdapterCompetitie = new SqlDataAdapter();

        DataSet dataSetCompetitie = new DataSet();

        SqlDataAdapter dataAdapterMeci = new SqlDataAdapter();

        DataSet dataSetMeci = new DataSet();
        public midTextBox()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                dataAdapterCompetitie.SelectCommand = new SqlCommand("SELECT * FROM Competitii", connection);
                dataSetCompetitie.Clear();
                dataAdapterCompetitie.Fill(dataSetCompetitie);
                dataGridViewParent.DataSource = dataSetCompetitie.Tables[0];

                stergereButton.Visible = true;
                actualizareButton.Visible = true;
                adaugareButton.Visible = false;

                /*dataAdapterMeci.SelectCommand = new SqlCommand("SELECT * FROM Meciuri", connection);
                dataSetMeci.Clear();
                dataAdapterMeci.Fill(dataSetMeci);
                dataGridViewChild.DataSource = dataSetMeci.Tables[0];*/



            }
            catch (Exception ex)
            {
                messageToUser.Text += ex.Message;
                messageToUser.ForeColor = Color.DarkRed;
                connection.Close();
            }

            /*stergereButton.Visible = false;
            actualizareButton.Visible = false;*/
            adaugareButton.Visible = false;
            /*competitieIdTextBox.Enabled = false;
            denumireTextBox.Enabled = false;
            idMeciTextBox.Enabled = false;
            idCompetitieTextBox.Enabled = false;*/

        }



        private void dataGridView_Competitie_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            stergereButton.Visible = false;
            actualizareButton.Visible = false;
            adaugareButton.Visible = true;
            echipeTextBox.Enabled = true;
            messageToUser.Text = "";
            idMeciTextBox.Text = "";
            echipeTextBox.Text = "";
            scorTextBox.Text = "";
            nrSpectatoriTextBox.Text = "";

            try
            {
                if (dataGridViewParent.Rows[e.RowIndex].Cells[e.ColumnIndex].Value != null) // Verificăm dacă este o celulă validă
                {
                    dataGridViewParent.CurrentRow.Selected = true;

                    idCompetitieTextBox.Text = dataGridViewParent.Rows[e.RowIndex].Cells["Cid"].FormattedValue.ToString();

                    // Filtrăm înregistrările din tabela Meciuri folosind Cid-ul selectat din tabela Competitii
                    dataAdapterMeci.SelectCommand = new SqlCommand("SELECT * FROM Meciuri WHERE Cid = @Cid", connection);
                    dataAdapterMeci.SelectCommand.Parameters.AddWithValue("@Cid", idCompetitieTextBox.Text);
            

                    dataSetMeci.Clear();
                    dataAdapterMeci.Fill(dataSetMeci);

                    dataGridViewChild.DataSource = dataSetMeci.Tables[0];
          
                }
            }
            catch (Exception ex)
            {
                connection.Close();
                messageToUser.Text = ex.Message;
                messageToUser.ForeColor = Color.DarkRed;
            }
        }

        private void dataGridView_Meci_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            messageToUser.Text = "";
            adaugareButton.Visible = false;
            stergereButton.Visible = true;
            actualizareButton.Visible = true;

            try
            {
                if (e.RowIndex >= 0 && e.ColumnIndex >= 0) // Verificăm dacă este o celulă validă
                {
                    dataGridViewChild.CurrentRow.Selected = true;

                    idMeciTextBox.Text = dataGridViewChild.Rows[e.RowIndex].Cells["Mid"].FormattedValue.ToString();
                    echipeTextBox.Text = dataGridViewChild.Rows[e.RowIndex].Cells["Echipe"].FormattedValue.ToString();
                    scorTextBox.Text = dataGridViewChild.Rows[e.RowIndex].Cells["Scor"].FormattedValue.ToString();
                    nrSpectatoriTextBox.Text = dataGridViewChild.Rows[e.RowIndex].Cells["NrSpectatori"].FormattedValue.ToString();
                    idCompetitieTextBox.Text = dataGridViewChild.Rows[e.RowIndex].Cells["Cid"].FormattedValue.ToString();
                }
            }
            catch (Exception ex)
            {
                messageToUser.Text = ex.Message;
                messageToUser.ForeColor = Color.DarkRed;
            }
        }

        private void stergereButton_Click(object sender, EventArgs e)
        {
            try
            {
                string Mid = dataGridViewChild.SelectedRows[0].Cells["Mid"].FormattedValue.ToString();

                dataAdapterMeci.DeleteCommand = new SqlCommand("DELETE FROM Meciuri WHERE Mid = @Mid", connection);
                dataAdapterMeci.DeleteCommand.Parameters.AddWithValue("Mid", Mid);

                connection.Open();
                dataAdapterMeci.DeleteCommand.ExecuteNonQuery();
                connection.Close();

                messageToUser.Text = "Meci sters cu succes!";
                messageToUser.ForeColor = Color.DarkRed;

                dataSetMeci.Clear();
                dataAdapterMeci.Fill(dataSetMeci);
            } catch (Exception ex)
            {
                connection.Close();
                messageToUser.Text = ex.Message;
                messageToUser.ForeColor= Color.DarkRed;
            }
        }


        private void actualizareButton_Click(Object sender, EventArgs e)
        {
            try
            {
                dataAdapterMeci.UpdateCommand = new SqlCommand("UPDATE Meciuri SET Echipe = @Echipe, Scor = @Scor, NrSpectatori = @NrSpectatori, Cid = @Cid WHERE Mid = @Mid", connection);
                dataAdapterMeci.UpdateCommand.Parameters.AddWithValue("@Mid", idMeciTextBox.Text);
                dataAdapterMeci.UpdateCommand.Parameters.AddWithValue("@Echipe", echipeTextBox.Text);
                dataAdapterMeci.UpdateCommand.Parameters.AddWithValue("@Scor", scorTextBox.Text);
                dataAdapterMeci.UpdateCommand.Parameters.AddWithValue("@NrSpectatori", nrSpectatoriTextBox.Text);
                dataAdapterMeci.UpdateCommand.Parameters.AddWithValue("@Cid", idCompetitieTextBox.Text);
                
                connection.Open();
                dataAdapterMeci.UpdateCommand.ExecuteNonQuery();
                connection.Close();

                dataSetMeci.Clear();
                dataAdapterMeci.Fill(dataSetMeci);

                messageToUser.Text = "Meci actualizat cu succes";
                messageToUser.ForeColor = Color.DarkGreen;
            }
            catch (Exception ex)
            {
                connection.Close();
                messageToUser.Text = ex.Message;
                messageToUser.ForeColor = Color.DarkRed;
            }
        }



        private void adaugareButton_Click(object sender, EventArgs e)
        {
            try
            {
                dataAdapterMeci.InsertCommand = new SqlCommand("INSERT INTO Meciuri(Echipe, Scor, NrSpectatori, Cid)" + "VALUES (@Echipe, @Scor, @NrSpectatori, @Cid)", connection);
                dataAdapterMeci.InsertCommand.Parameters.AddWithValue("Echipe", echipeTextBox.Text);
                dataAdapterMeci.InsertCommand.Parameters.AddWithValue("Scor", scorTextBox.Text);
                dataAdapterMeci.InsertCommand.Parameters.AddWithValue("NrSpectatori", nrSpectatoriTextBox.Text);
                dataAdapterMeci.InsertCommand.Parameters.AddWithValue("Cid", idCompetitieTextBox.Text);

                connection.Open();
                dataAdapterMeci.InsertCommand.ExecuteNonQuery();
                connection.Close();

                dataSetMeci.Clear();
                dataAdapterMeci.Fill(dataSetMeci);

                messageToUser.Text = "Meci adaugat cu succes!";
                messageToUser.ForeColor = Color.DarkRed;

            } catch(Exception ex)
            {
                connection.Close();
                messageToUser.Text = ex.Message;
                messageToUser.ForeColor= Color.DarkRed;
            }
            
        }

        private void scorTextBox_TextChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }
    }
}



